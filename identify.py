"""
Updated 02-FEB-2021

sys.argv[1] = name and path of the ESRI datafile
sys.argv[2] = float or integer of the vertical accuracy threshold

identify.py:
Extract user guides from hard coded data in MCD12_user_guide_to_dfs.py.

Extract Latitude, Longitude, Fix Time, Edit Date from ESRI datafile.

Pass lat and long into MODIS web query. Match to all uer guide's
Board of Classification's landtypes. Save results to a JSON file.

Query Daymet weatherdata with cleaned ERSI data by Latitude, Longitude,
Fix Time, and Edit Date. Save results to a JSON file.


"""
import sys
import json
import datetime
import requests
#import geojson
#import asyncio
import pandas as pd
#import pandasql as ps
import MCD12_user_guide_to_dfs as ug
# import classification_testing_data as ctd  # remove from production ver.

def getModisDates(date_start, date_end):
    date_start = date_start.split('-')
    date_start = datetime.date(int(date_start[0]),int(date_start[1]),int(date_start[2]))
    date_end = date_end.split('-')
    date_end = datetime.date(int(date_end[0]),int(date_end[1]),int(date_end[2]))
    day_of_year_start = date_start.strftime('%j')
    day_of_year_end = date_end.strftime('%j')
    year_start = str(date_start.year)
    year_end =   str(date_end.year)
    modis_start = 'A'+year_start + day_of_year_start
    modis_end = 'A' + year_end + day_of_year_end
    return '&startDate=' + modis_start+ '&endDate=' + modis_end

"""
clean_esri_data
@author: Dan Hopp, Stan Martin

Pull Latitude and Longitude collector data if:
    Receiver Name is not blank.
    Creation Date (col 25) and Fix Time (col 19) are within 1 minute (inclusive).
    Vertical Accuracy (m) (col 8) is < user specified (exclusive).

Insert Lat and Long into a dataframe, and then export it to a .csv file. Allow
the user to specify the Virtical Accuracy threshold (exclusive).

Created on Wed Jan 13 18:27:42 2021
Updated Thurs Jan 14 2021 - Made it a function, added try-except, and
added export
Updated Thurs Jan 21 2021 - Replace export with return a dataframe
Updated Fri Jan 22 2021 - adjusted for different date formats
Updated Fri Jan 29 2021 - Added Fix Time and Edit Date columns to the extaction
Updated Tues Feb 2 2021 - Added a softcoded file name, sys.argv[1]

"""
def clean_esri_data(file_path, va_threshold):
    #datetime help from https://www.educative.io/edpresso/how-to-convert-a-
    #  string-to-a-date-in-python
    from datetime import datetime
    from datetime import timedelta

    try:
        # making dataframe from csv file
        df = pd.read_csv(file_path)

        # create dataframe to hold Latitude and Longitude
        esri_df = pd.DataFrame(columns = ['Latitude', 'Longitude',
                                          'Fix Time', 'EditDate'])
        # print(df)
        # help with NaN and column iteration
        # borrowed from https://stackoverflow.com/questions/41287171/iterate-
        #through-dataframe-and-select-null-values
        for index, row in df.iterrows():
            # if Receiver Name (col 6) is NaN, ignore row
            if pd.notnull(row['Receiver Name']):
                # pull Latitude and Longitude (columns 9 and 10) if:
                  # Creation Date (col 25) and Fix Time (col 19) are within 1 minute
                  # of each other.
                  # Vertical Accuracy (m) (col 8) is < user specified (exclusive).
                      #
                if float(row['Vertical Accuracy (m)']) < float(va_threshold):
                    # what date format does the file have?
                    if row['CreationDate'].find('/') != -1:
                        # convert strings to datetime
                        creation_date_obj = datetime.strptime(row['CreationDate'],
                                                              '%m/%d/%Y %H:%M')
                        fix_time_obj = datetime.strptime(row['Fix Time'],
                                                          '%m/%d/%Y %H:%M')
                    else:
                        creation_date_obj = datetime.strptime(row['CreationDate'],
                                                              '%Y-%m-%d %H:%M')
                        fix_time_obj = datetime.strptime(row['Fix Time'],
                                                          '%Y-%m-%d %H:%M')
                if creation_date_obj - fix_time_obj <= timedelta(minutes=1):
                    esri_df = esri_df.append({'Latitude' : row['Latitude'],
                                          'Longitude' : row['Longitude'],
                                          'Fix Time' : row['Fix Time'],
                                          'EditDate' : row['EditDate']},
                                          ignore_index = True)
        # print(esri_df)
        return esri_df
    except ValueError as verr:
        print('ValueError:', verr)
    except TypeError as terr:
        print('TypeError:', terr)
    except KeyError as kerr:
        print('A column in the file is missing or has moved:')
        print(kerr)
    except FileNotFoundError:
        print('The import file was not found!')
    except:
        print('Unexpected error:', sys.exc_info()[0])
        

def get_landcover(lat,long,modisDateQuery):

    # create dataframe to hold Class and Description
    class_desc = pd.DataFrame(columns = ['Class', 'Description'])

    query = (MODIS_BASE+'MCD12Q1/subset?latitude='+lat+'&longitude='+long+
             modisDateQuery+'&kmAboveBelow=0&kmLeftRight=0')
    #print (query);
    response = requests.get(query, headers=header)
    if response.status_code == 200:
        res = json.loads(response.content.decode('utf-8'))
        subset = res["subset"]
        for x in subset:
            i = 1
            band = x["band"].strip()
            data = x["data"]
            if len(data) == 1:
                val = str((data[0]))
                # print(band)
                # print(data)
                ClassificationType = table1['Description'][table1.index == band]
                CL =(ClassificationType[band])
                # print(CL)
                if "IGBP" in CL:
                    IGB = get_classification(val, table3)
                    # print(IGB, CL)
                elif "UMD" in CL:
                    IGB = get_classification(val, table4)
                    # print(IGB, CL)
                elif "LAI" in CL:
                    IGB = get_classification(val, table5)
                    # print(IGB, CL)
                elif "BGC" in CL:
                    IGB = get_classification(val, table6)
                    # print(IGB, CL)
                elif "PFT" in CL:
                    IGB = get_classification(val, table7)
                    # print(IGB, CL)
                # LC_Prop#_Assessment ###################
                elif "LCCS1 land cover layer confidence" in CL:
                    IGB = ('Confidence ' + val + ' percent.', CL)
                    # print(IGB, CL)
                elif "LCCS2 land use layer confidence" in CL:
                    IGB = ('Confidence ' + val + ' percent.', CL)
                    # print(IGB, CL)
                elif "LCCS3 surface hydrology layer confidence" in CL:
                    IGB = ('Confidence ' + val + ' percent.', CL)
                    # print(IGB, CL)
                #########################################################
                elif "LCCS1 land cover layer" in CL:
                    IGB = get_classification(val, table8)
                    # print(IGB, CL)
                elif "LCCS2 land use layer" in CL:
                    IGB = get_classification(val, table9)
                    # print(IGB, CL)
                elif "LCCS3 surface hydrology layer" in CL:
                    IGB = get_classification(val, table10)
                    # print(IGB, CL)
                elif "Product quality flags" in CL:
                    IGB = get_classification(val, table11)
                    # print(IGB, CL)
                    #LW
                elif "Binary land (class 2) / water (class 1)" in CL:
                    IGB = ('Binary land (class 2) / water (class 1)',
                          'Binary land (class 2) / water (class 1)')

                # populate table with class and description
                class_desc = class_desc.append({'Class' : CL,
                                                'Description' : IGB},
                                                ignore_index = True)
                data = data[0]

        #export class_desc table to JSON file
        class_desc.to_json("Class_Descriptions_" + str(i) + ".json",
                            orient="values")
        i += 1
    else:
        return response.status_code

    return 'Class Description JSON file exported.'


# #### Function for testing ###########################################
# def get_landcover_band_testing(lat,long,modisDateQuery):
# #     data = [1]
# #     band = 'LC_Type1'
# #     # band = 'LC_Type2'
# #     # band = 'LC_Type3'
# #     # band = 'LC_Type4'
# #     # band = 'LC_Type5'
# #     # band = 'LC_Prop1'
# #     # band = 'LC_Prop2'
# #     # band = 'LC_Prop3'
# #     # band = 'LC_Prop1_Assessment'
# #     # band = 'LC_Prop2_Assessment'
# #     # band = 'LC_Prop3_Assessment'
# #     # band = 'QC'
# #     # band = 'LW'

#     ########### delete ######################
#     subset = ctd.get_subset_test_data()
#     # res = json.loads(chikin.decode('utf-8'))
#     # subset = res["subset"]
#     ##########################################
#     # create dataframe to hold Class and Description
#     class_desc = pd.DataFrame(columns = ['Class', 'Description'])
#     for index, row in subset.iterrows():
#         i = 1
#         band = row['band']
#         data = row['data']

#         print('**************BEGIN LINE*********************')

#         print(band)
#         print(data)
#         ClassificationType = table1['Description'][table1.index == band]
#         CL =(ClassificationType[band])
#         print(CL)
#         if len(data) == 1:
#             val = str((data[0]))
#             if "IGBP" in CL:
#                 # print('IGBP:')
#                 IGB = get_classification(val, table3)
#                 # print(IGB, CL)
#             elif "UMD" in CL:
#                 # print('UMD:')
#                 IGB = get_classification(val, table4)
#                 # print(IGB, CL)
#             elif "LAI" in CL:
#                 # print('LAI:')
#                 IGB = get_classification(val, table5)
#                 # print(IGB, CL)
#             elif "BGC" in CL:
#                 # print('BGC:')
#                 IGB = get_classification(val, table6)
#                 # print(IGB, CL)
#             elif "PFT" in CL:
#                 # print('PFT:')
#                 IGB = get_classification(val, table7)
#                 print(IGB, CL)
#             # LC_Prop#_Assessment ###################
#             elif "LCCS1 land cover layer confidence" in CL:
#                 # print('LCCS1 land cover layer confidence:')
#                 IGB = ('Confidence ' + val + ' percent.', CL)
#                 print(IGB, CL)
#             elif "LCCS2 land use layer confidence" in CL:
#                 # print('LCCS2 land use layer confidence:')
#                 IGB = ('Confidence ' + val + ' percent.', CL)
#                 print(IGB, CL)
#             elif "LCCS3 surface hydrology layer confidence" in CL:
#                 # print('LCCS3 surface hydrology layer confidence:')
#                 IGB = ('Confidence ' + val + ' percent.', CL)
#                 print(IGB, CL)
#             #################################################################
#             elif "LCCS1 land cover layer" in CL:
#                 # print('LCCS1 land cover layer:')
#                 IGB = get_classification(val, table8)
#                 print(IGB, CL)
#             elif "LCCS2 land use layer" in CL:
#                 # print('LCCS2 land use layer:')
#                 IGB = get_classification(val, table9)
#                 print(IGB, CL)
#             elif "LCCS3 surface hydrology layer" in CL:
#                 # print('LCCS3 surface hydrology layer:')
#                 IGB = get_classification(val, table10)
#                 print(IGB, CL)
#             elif "Product quality flags" in CL:
#                 # print('Product quality flags:')
#                 IGB = get_classification(val, table11)
#                 print(IGB, CL)
#                 #LW
#             elif "Binary land (class 2) / water (class 1)" in CL:
#                 IGB = ('Binary land (class 2) / water (class 1)',
#                         'Binary land (class 2) / water (class 1)')

#             # populate table with class and description
#             class_desc = class_desc.append({'Class' : CL, 'Description' : IGB},
#                                             ignore_index = True)
#             data = data[0]
#             print(data)
#             # print (band)
#             print('**************END LINE*********************')
#             print()
#     #export class_desc table to JSON file
#     class_desc.to_json("Class_Descriptions_" + str(i) + ".json",
#                         orient="values")
#     i += 1
# ##########################################################################

# query User Guide Classification tables using Value column
def get_classification(val, table):
    # if len(data) == 1:
    try:
        # val = (data[0])
        N = table.loc[table['Value'] == val, 'Name'].iloc[0]
        D = table.loc[table['Value'] == val, 'Description'].iloc[0]
        return N, D
    except IndexError:
        print('No value ' + val + ' found in the table!')
        return 'No_Value_Found', 'No_Value_Found'

# Date to string functions
def getDateFromString(date):
    if date.find('/') != -1:
        return datetime.datetime.strptime(date, '%m/%d/%Y %H:%M')
    else:
        return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
def getMonthFromString(date):
    return str(date.month)
def getDayFromString(date):
    return str(date.day)
def getYearFromString(date):
    return str(date.year)

# fix time = start date, edit date = end date
def getDaymetDaterangeURL(fix_time, edit_date):

    date_ft = getDateFromString(fix_time)
    date_ed = getDateFromString(edit_date)

    date_start_month = getMonthFromString(date_ft)
    date_start_day = getDayFromString(date_ft)
    date_start_year = getYearFromString(date_ft)

    date_end_month = getMonthFromString(date_ed)
    date_end_day = getDayFromString(date_ed)
    date_end_year = getYearFromString(date_ed)

    # build string '&start=2012-01-31&end=2012-01-31
    # dates_url = ('years=' + date_start_year + '&start=' + date_start_month +
    #              '%2F' + date_start_day + '%2F' + date_start_year + '&end=' +
    #              date_end_month + '%2F' + date_end_day + '%2F' +
    #              date_end_year + '&')
    dates_url = ('&start=' + date_start_year + '-' + date_start_month + '-' +
                 date_start_day +
                 '&end=' + date_end_year + '-' + date_end_month + '-' +
                 date_end_day)
    return dates_url



#https://daymet.ornl.gov/single-pixel/api/data?lat=43.1&lon=-85.3&format=
#json&start=2012-01-31&end=2012-01-31
# query daymet page for weather data by lat, long,
# and MODIS fix time(start date), edit date (end date)
def get_daymet(lat, long, date_start, date_end):
    url = ('https://daymet.ornl.gov/single-pixel/api/data?lat=' + lat +
           '&lon=' + long + '&format=json' +
           getDaymetDaterangeURL(date_start, date_end))
    query = url
    response = requests.get(query, headers=header)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


###### BEGIN IDENTIFY.PY ################################

# base URL for MODIS website query
MODIS_BASE = 'https://modis.ornl.gov/rst/api/v1/'       

#header for MODIS website query
header = {'Content-Type':'application/json'}

#date range for MODIS website query
DATE_START ='2010-01-01'
DATE_END = '2010-12-31'

#call funtion to create date range URL for MODIS query
modisDateQuery = getModisDates(DATE_START,DATE_END)
# #print(modisDateQuery)


# get clean esri data and pass into a dataframe
clean_esri_data_df = clean_esri_data(sys.argv[1], sys.argv[2])

# unused(?)
PRODUCT = 'MCD12Q1/'


#endpoint = 'products';

######## 27-JAN-2021 .pdf extraction replaced with a hard-coded module #####
# from tabula.io import read_pdf
# PDF_PATH = "MCD12_User_Guide_V6.pdf"
# dfs = read_pdf(PDF_PATH, multiple_tables=True, lattice=True, pages="all")
# #for loop code borrowed from https://stackoverflow.com/questions/49733576/
#     #how-to-extract-more-than-one-table-present-in-a-pdf-file-with-tabula-
#     #in-python
# #print (len(dfs));
# #print (type(dfs[2]));
# #rint (dfs[0].columns);
# table1 = dfs[0].dropna()
# table2 = dfs[1].dropna()
# table3 = dfs[2].dropna()
# table4 = dfs[3].dropna()
# table5 = dfs[4].dropna()
# table6 = dfs[5].dropna()
# table7 = dfs[6].dropna()
# table8 = dfs[7].dropna()
# table9 = dfs[8].dropna()
# table10 = dfs[9].dropna()
# table11 = dfs[10].dropna()
# table12 = dfs[11].dropna()
#######################################################################

# create the user guide tables
table1 = ug.MCD12_user_guide()[0]
table2 = ug.MCD12_user_guide()[1]
table3 = ug.MCD12_user_guide()[2]
table4 = ug.MCD12_user_guide()[3]
table5 = ug.MCD12_user_guide()[4]
table6 = ug.MCD12_user_guide()[5]
table7 = ug.MCD12_user_guide()[6]
table8 = ug.MCD12_user_guide()[7]
table9 = ug.MCD12_user_guide()[8]
table10 = ug.MCD12_user_guide()[9]
table11 = ug.MCD12_user_guide()[10]
table12 = ug.MCD12_user_guide()[11]

# set indexes for the Data Set tables
table1.set_index('Short_Name', inplace = True)
table2.set_index('Short_Name', inplace = True)


#### OLD CODE FOR WHEN THE USER GUIDES WERE IMPORTED VIA .PDF #######
# i=1
# for table in dfs:
#     table.columns = table.iloc[0]
#     table = table.reindex(table.index.drop(0)).reset_index(drop=True)
#     table.columns.name = None
# #To write CSV
#     #table.to_csv('MCD12Q1_table'+str(i)+'.csv',sep=',',header=True,index=False)
#     i=i+1
#######################################################################

# pass
#lat = sys.argv[1];

#long = sys.argv[2];
#DATE_START = sys.argv[3];
#DATE_END = sys.argv[4];

#print (lat + long + BeginDate + EndDate);
#Parameters that should be supplied by some user interface

#JSON lat longs
#infile = open ('C:\\Users\\msk\\Desktop\\CBI\\DATA\\commongardens\\CG_centroids.geojson','r');

#data = geojson.load(infile);

#for coordinates in data:
#    print (coordinates);



# loop through clean esri data coords to print landcover results
for df_index, r in clean_esri_data_df.iterrows():
    LAT = str(r['Latitude'])
    LONG = str(r['Longitude'])
    # response = requests.get('https://modis.ornl.gov/rst/api/v1/MCD12Q1/dates?latitude='+
    #                          LAT + '&longitude=' + LONG, headers=header)
    landcover = get_landcover(LAT, LONG, modisDateQuery)
    # landcover = get_landcover_band_testing(LAT, LONG, modisDateQuery)
    print (landcover)


######## commented out 21-JAN-2021 #################
# dates = json.loads(response.text)['dates']
# #print(dates);
# modis_dates = [i['modis_date'] for i in dates]
# calendar_dates = [i['calendar_date'] for i in dates]
#####################################################




#### 31-JAN-2021: TEMP DESABLED TO ALLOW for daymetTesting() #############
# # loop through clean_esri dates and data coords to export
# # weather data to a JSON file
# for df_index, r in clean_esri_data_df.iterrows():
#     i = 1
#     LAT = str(r['Latitude'])
#     LONG = str(r['Longitude'])
#     FIX_TIME = str(r['Fix Time'])
#     EDIT_DATE = str(r['EditDate'])
#     #hardcode dates for testing
#     # daymet = get_daymet(LAT, LONG, '10/15/2019 13:05', '10/15/2019 13:06')
#     daymet = get_daymet(LAT, LONG, FIX_TIME, EDIT_DATE)
#     # print (daymet)
#     # create file date string
#     file_date = getDateFromString(FIX_TIME)
#     file_date_str = (getYearFromString(file_date) + '-' +
#                     getMonthFromString(file_date)  + '-' +
#                     getDayFromString(file_date))
#     with open('weatherdata_' + str(i) + '_lat_' + LAT + '_lon_' + LONG + '_' +
#               file_date_str + '.json', 'w') as f:
#         json.dump(daymet, f)
#     i += 1
##################################################################

# Daymet testing
def daymetTesting():
    i = 1
    LAT = '35.84406013'
    LONG = '-83.95906955'
    FIX_TIME = '10/15/2019 13:05'
    EDIT_DATE = '10/15/2019 13:06'
    #hardcode dates for testing
    daymet = get_daymet(LAT, LONG, FIX_TIME, EDIT_DATE)
    # print (daymet)

    # create file date string
    file_date = getDateFromString(FIX_TIME)
    file_date_str = (getYearFromString(file_date) + '-' +
                    getMonthFromString(file_date)  + '-' +
                    getDayFromString(file_date))

    with open('weatherdata_' + str(i) + '_lat_' + LAT + '_lon_' + LONG + '_' +
              file_date_str + '.json', 'w') as f:
        json.dump(daymet, f)

daymetTesting()
print('Weatherdata JSON is exported.')