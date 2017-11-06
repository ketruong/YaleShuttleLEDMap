#from util import *
#from transloc_data import *
from api import *
#import dateutil.parser as dp
#from color import *
req = STOPS_BY_ROUTES['Red']
for i in req:
   print i['name']
#x = STOPS_BY_ROUTES['Blue Night']
#for i in x:
#    print i['name']
#for buses in req.values():
#    for bus in buses:
#        t = bus['last_updated_on'] 
#        parsed_t = dp.parse(t)
#        t_in_seconds = parsed_t.strftime('%s')
#        print type(t_in_seconds)
#        print t_in_seconds



