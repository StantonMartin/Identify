import json
import requests
import geojson

#Parameters that should be supplied by some user interface

#JSON lat longs
infile = open ('C:\\Users\\msk\\Desktop\\CBI\\DATA\\commongardens\\CG_centroids.geojson','r');

data = geojson.load(infile);

#for coordinates in data:
#    print (coordinates);

product = 'MCD12Q1/'
modis_base = 'https://modis.ornl.gov/rst/api/v1/';

#endpoint = 'products';

header = {'Content-Type':'application/json'};


response = requests.get('https://modis.ornl.gov/rst/api/v1/MCD12Q1/dates?latitude=39.56499&longitude=-121.55527', headers=header)
#print(response);
dates = json.loads(response.text)['dates']

modis_dates = [i['modis_date'] for i in dates]
calendar_dates = [i['calendar_date'] for i in dates]

long = '-119.561634';
lat ='45.833493'
dateStart ='2001-01-01';
dateEnd = '2017-01-01';
modisStart = 'A2001001';
modisEnd = 'A2001365'
def get_landcover(lat,long,modisStart,modisEnd):

    query = modis_base+'MCD12Q1/subset?latitude='+lat+'&longitude='+long+'&startDate='+modisStart+'&endDate='+modisEnd+'&kmAboveBelow=0&kmLeftRight=0';
    print (query);
    response = requests.get(query, headers=header)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

landcover =  get_landcover(lat,long,modisStart,modisEnd);
print (landcover)


