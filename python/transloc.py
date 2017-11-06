import math
import time
from  api import * 
from transloc_data import *
from util import *
import dateutil.parser as dp
#http://realtime.mbta.com/Portal/Content/Documents/MBTA-realtime_APIDocumentation_v2_1_4_2017-03-08.pdf


class Route(object):
    def __init__(self, stations, name, api_name=None):
        self.name = name
        self.api_name = api_name or name
        self.stations = list()
	for i in ROUTES[name]:
	    try:
		 self.stations.append(stations.get(i))
	    except:
		d = 0
	self.stations_dict = {}
	
        for st in self.stations:
            self.stations_dict[st.name] = st
    def get_trains(self):
        trains = []
        req = vehiclesByID(VEHICLES_BY_ROUTES[self.api_name]) 
        if req is None: 
            return []
        for train in req.values():
            for bus in train:
                t = bus['last_updated_on'] 
                parsed_t = dp.parse(t)
                t_in_seconds = parsed_t.strftime('%s')
                trains.append(Train(
                    bus['call_name'],
                    bus['vehicle_id'],
                    (
                        float(bus['location']['lat']),
                        float(bus['location']['lng'])
                    ),
                    int('0'),
                    int(t_in_seconds)
                ))
        return trains

    def locate_train(self, train):
        between = min(
            pairwise(self.stations),
            key=lambda (a, b): point_line_segment_distance(a.location, b.location, train.location)
        )
        progress = point_distance(
            train.location,
            between[0].location
        ) / point_distance(
            between[0].location,
            between[1].location
        )
        if train.direction == 1:
            between = tuple(reversed(between))
            progress = 1 - progress
        return (between[0], between[1], progress)


class Routes(object):
    def __init__(self, stations):
        self.routes = {} 
        
	for k in API_ROUTE_NAMES:
	#    print k
	#    print stations 
            self.routes[k] = Route(stations, k, API_ROUTE_NAMES[k])

    def all(self):
        for k in self.routes:
            yield self.routes[k]

    def get(self, name):
        return self.routes[name]


class Train(object):
    def __init__(self, name, id, location, direction, timestamp):
        self.name = name
        self.id = id
        self.location = location
        self.direction = direction
        self.measurements = 1
        self.last_velocity = 0
        self.average_velocity = 0
        self.timestamp = timestamp


class Station(object):
    def __init__(self, name, location):
        self.lines = set()
        self.name = name
        self.location = location

    def __str__(self):
        return self.name

    def transfer_station(self):
        return len(self.lines) > 1


class Stations(object):
    def __init__(self):
        self.stations = {}
        '''
        govt_center = Station('Government Center', (42.359444, -71.059444))
        self.stations['Government Center'] = govt_center
        self.stations['Government Center'].lines = set(['Green', 'Blue'])
        '''
        #look at previous three lines because that's what happening
        for route in API_ROUTE_NAMES.values():
            stops = STOPS_BY_ROUTES[route]
	    if stops is None:
		print hi
	    else:
            # print res
            #stops = res['direction'][0]['stop']
		for stop in stops:
		    name = stop['name']
		    station = Station(
			    name, (float(stop['location']['lat']), float(stop['location']['lng'])))
		    if not self.stations.get(name):
			self.stations[name] = station
		    #self.stations[name].lines.add(route.split('-')[0])

    def get(self, name):
        return self.stations[name]

    def get_location(self, name):
        station = self.stations.get(name)
        if not station:
            return False
        else:
            return station.location
