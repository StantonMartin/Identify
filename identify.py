import json
import requests
import geojson
import sys
import asyncio
import datetime
#import pandas as pd
#import pandasql as ps


from tabula.io import read_pdf
pdf_path = "MCD12_User_Guide_V6.pdf"

dfs = read_pdf(pdf_path, multiple_tables=True, lattice=True, pages="all")
#for loop code borrowed from https://stackoverflow.com/questions/49733576/how-to-extract-more-than-one-table-present-in-a-pdf-file-with-tabula-in-python
#print (len(dfs));
#print (type(dfs[2]));
#rint (dfs[0].columns);
table1 = dfs[0].dropna();
table2 = dfs[1].dropna();
table3 = dfs[2].dropna();
table4 = dfs[3].dropna();
table5 = dfs[4].dropna();
table6 = dfs[5].dropna();
table7 = dfs[6].dropna();
table8 = dfs[7].dropna();
table9 = dfs[8].dropna();
table10 = dfs[9].dropna();
table11 = dfs[10].dropna();
table12 = dfs[11].dropna();


print (table1["Short\rName"]);
#print (dfs[0]);

for table in dfs:
    #print (table)
    pass
#lat = sys.argv[1];

#long = sys.argv[2];
#dateStart = sys.argv[3];
#dateEnd = sys.argv[4];

#print (lat + long + BeginDate + EndDate);
#Parameters that should be supplied by some user interface

#JSON lat longs
#infile = open ('C:\\Users\\msk\\Desktop\\CBI\\DATA\\commongardens\\CG_centroids.geojson','r');

#data = geojson.load(infile);

#for coordinates in data:
#    print (coordinates);

product = 'MCD12Q1/'
modis_base = 'https://modis.ornl.gov/rst/api/v1/';

#endpoint = 'products';

header = {'Content-Type':'application/json'};


response = requests.get('https://modis.ornl.gov/rst/api/v1/MCD12Q1/dates?latitude=39.56499&longitude=-121.55527', headers=header)

dates = json.loads(response.text)['dates']
#print(dates);
modis_dates = [i['modis_date'] for i in dates]
calendar_dates = [i['calendar_date'] for i in dates]

long = '-119.561634';
lat ='45.833493'
dateStart ='2001-01-01';
dateEnd = '2010-12-31';

def getModisDates(dateStart, dateEnd):
    dateStart = dateStart.split('-');
    dateStart = datetime.date(int(dateStart[0]),int(dateStart[1]),int(dateStart[2]))
    dateEnd = dateEnd.split('-')
    dateEnd = datetime.date(int(dateEnd[0]),int(dateEnd[1]),int(dateEnd[2]))
    day_of_year_Start = dateStart.strftime('%j')
    day_of_year_End = dateEnd.strftime('%j')
    yearStart = str(dateStart.year)
    yearEnd =   str(dateEnd.year)
    modisStart = 'A'+yearStart + day_of_year_Start;
    modisEnd = 'A' + yearEnd + day_of_year_End
    return '&startDate=' + modisStart+ '&endDate=' + modisEnd

modisDateQuery = getModisDates(dateStart,dateEnd)
#print(modisDateQuery)


def get_landcover(lat,long,modisDateQuery):

    query = modis_base+'MCD12Q1/subset?latitude='+lat+'&longitude='+long+modisDateQuery+'&kmAboveBelow=0&kmLeftRight=0';
    print (query);
    response = requests.get(query, headers=header)
    if response.status_code == 200:
        res = json.loads(response.content.decode('utf-8'))
        subset = res["subset"]
        for x in subset:
            band = x["band"].strip();
            band = band.replace('_',' ');
            print(band);
            ClassificationType = table1["Description"][table1["Short\rName"][0] == band];
            print (ClassificationType[0]);
            #data = data[0]
            #print (band)
            #


    else:
        return response.status_code

landcover =  get_landcover(lat,long,modisDateQuery);
#print (landcover)

def get_daymet(lat,long,dateStart,dateEnd):
    query = 'https://daymet.ornl.gov/single-pixel/api/data?lat=45.833493&lon=-119.561634&vars=&format=json';
    response = requests.get(query, headers=header)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

daymet = get_daymet(lat,long,dateStart,dateEnd)
#print(daymet);
