#API methods and constants
import unirest
import json
#import transloc_data
api_header = {
        "X-Mashape-Key": "MvVwHz4aP4mshYXZfLEHw1nUjve2p1OWr1sjsnMtX0AuJgR29q",
        "Accept": "application/json" 
        }
api_url = "https://transloc-api-1-2.p.mashape.com/"
api_agencies = "agencies=yale"
api_callback = "callback=call"
api_geo_area = "geo_area=41.3%2C-72.9%7C5000"
params = api_agencies + "&"+ api_callback + "&"+ api_geo_area 

#VBR = vehicles by route
api_VBR = api_url + "vehicles.json?"+ params + "&"+ "routes="

BLUE_DAY_ID = "4000346"
BLUE_NIGHT_ID= "4000394"
GREEN_LINE_ID = "4000386"
RED_ID =  "4000342"
ORANGE_DAY_ID= "4000366" 
ORANGE_NIGHT_ID = "4000390" 
ORANGE_AFTERNOON_ID = "4000378"

def vehiclesByID(ID):
    return  json.loads(unirest.get(api_VBR + ID, headers=api_header).raw_body)['data']

VEHICLES_BY_ROUTES = {
        'Blue Day': (BLUE_DAY_ID),
        'Blue Night': (BLUE_NIGHT_ID),
        'Red': (RED_ID),
        'Orange Day': (ORANGE_NIGHT_ID),
        'Orange Night': (ORANGE_NIGHT_ID),
        'Orange Afternoon': (ORANGE_AFTERNOON_ID),
}

#Stops by route
api_SBR = api_url + "stops.json?"+ params 

response = unirest.get(api_SBR,headers=api_header)
stops = json.loads(response.raw_body)

def stopsbyID(ID):
    data=[]
    for stop in stops['data']:
        if ID in stop['routes']: 
            data.append(stop)
    return data    

STOPS_BY_ROUTES = {
        'Blue Day': stopsbyID(BLUE_DAY_ID),
        'Blue Night': stopsbyID(BLUE_NIGHT_ID),
        'Red': stopsbyID(RED_ID),
        'Orange Day': stopsbyID(ORANGE_DAY_ID),
        'Orange Night': stopsbyID(ORANGE_NIGHT_ID),
        'Orange Afternoon': stopsbyID(ORANGE_AFTERNOON_ID),
}
