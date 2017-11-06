class MapColors:
    RED = 0xFF0000
    GREEN = 0x00FF00
    BLUE = 0x0000FF
    ORANGE = 0xFFA500
    PURPLE = 0x551A8B

BRIGHTNESS_MULTIPLIERS = {
        #MapColors.RED: 1,
        #MapColors.ORANGE: 0.75,
        MapColors.BLUE: 0.5,
        #MapColors.GREEN: 0.5,
        #MapColors.PURPLE: 0.75
        }

BRIGHTNESS = 0.3
FADE_SIZE = 1
FADE_GRANULARITY = 0.1

SLEEP_TIME = 0.015
#ports on raspberry pi
#PORTS = ['/dev/serial0']
PORTS = ['/dev/ttyACM0', '/dev/ttyACM1']

ON_HOUR = 8
OFF_HOUR = 24
#something to do with api and names
API_ROUTE_NAMES = {
        'Blue Day': 'Blue Day',
        'Blue Night': 'Blue Night',
        'Red': 'Red',
        'Orange Day': 'Orange Day',
        'Orange Night': 'Orange Night',
        'Orange Afternoon': 'Orange Afternoon',
        }


#stations with stops 
ROUTES = {
        'Blue Day': [
            '333 Cedar',
            'Chapel/York',
            'College/Wall (Northbound)',
            '135 Prospect',
            'Chemistry/225 Prospect (N) /SCL',
            'Divinity/409 Prospect (Northbound)',
            'Prospect/Canner',
            'Whitney/Highland',
            'Whitney/Cottage',
            'Peabody Museum/ Whitney/Sachem',
            'Helen Hadley Hall',
            'College/Wall (Southbound)',
            'Phelps Gate',
            'LEPH/60 College',
            'Becton/15 Prospect',
            'Lot 22 (Whitney/Humphrey)',
            'Boyer Center',
            'Canner/Whitney',
            'Pierson Sage Garage',
            'Congress/Cedar',
            '129 York',
            'Prospect / Edwards (Yale Garden)',
            '300 George',
            'College/Crown',
            'Elm/York',
            'Prospect/Highland',
            'Whitney/Huntington',
            'Whitney/Linden',
            'Prospect / Trumbull',
            'Huntington / Edgehill',
            'Whitney/Cold Spring'
            ],
        'Blue Night': [
            '333 Cedar',
            'Chapel/York',
            'College/Wall (Northbound)',
            '135 Prospect',
            'Peabody Museum/ Whitney/Sachem',
            'Helen Hadley Hall',
            'College/Wall (Southbound)',
            'Phelps Gate',
            'LEPH/60 College',
            'CSS',
            'Broadway/Park',
            'Lot 22 (Whitney/Humphrey)',
            'HGS/320 York',
            'PWG/Tower Pkwy',
            'Union Station (Southbound)',
            'Congress/Cedar',
            '129 York',
            '300 George',
            'College/Crown',
            'Elm/York',
            'Church/George',
            '81 George St.'
            ],
         'Red':[
            'College/Wall (Northbound)',
            'Chemistry/225 Prospect (N) /SCL',
            'College/Wall (Southbound)',
            'Phelps Gate',
            'LEPH/60 College',
            'Union Station (Northbound)',
            'CSS',
            '25 Science Park',
            'Division/Prospect',
            'Amistad/Cedar',
            'State St Station',
            'Whitney/Audubon',
            'Yale Health Plan',
            'Court/Olive',
            'Olive/Chapel',
            '344 Winchester',
            'Chapel/Church',
            'TAC',
            'Chapel/College',
            '300 George',
            'College/Crown',
            'Prospect/Sachem',
            'Trumbull/Hillhouse',
            'Wall/Church',
            'Whitney/Grove',
            'Winchester/Tilton',
            'Winchester/Woodland',
            'Prospect/Hillside',
            'Winchester/Division'
                
            ],
        'Orange Day':[
            '333 Cedar',
            'Chapel/York',
            'College/Wall (Northbound)',
            '135 Prospect',
            'College/Wall (Southbound)',
            'Phelps Gate',
            'LEPH/60 College',
            'Orange/Humphrey (Southbound)',
            'Willow/Foster',
            'Foster/Edwards',
            'Canner/Whitney',
            'Orange/Willow (Southbound)',
            'Orange/Canner',
            'Edwards/Orange',
            'Orange/Pearl (Southbound)',
            'Pierson Sage Garage',
            'Congress/Cedar',
            '129 York',
            'Prospect / Edwards (Yale Garden)',
            '300 George',
            'Audubon/Orange',
            'College/Crown',
            'Foster/Cottage',
            'Grove/Temple',
            'Grove/Whitney',
            'Whitney / Edwards'
        ],
        'Orange Night':[
            '333 Cedar',
            'Chapel/York',
            'College/Wall (Northbound)',
            'College/Wall (Southbound)',
            'Phelps Gate',
            'LEPH/60 College',
            'Orange/Humphrey (Southbound)',
            'CSS',
            'Lot 22 (Whitney/Humphrey)',
            'Canner/Whitney',
            'Edwards/Orange',
            'Orange/Pearl (Southbound)',
            'Pierson Sage Garage',
            'Congress/Cedar',
            'Amistad/CSS',
            '129 York',
            '300 George',
            'Audubon/Orange',
            'College/Crown',
            'Grove/Temple',
            'Grove/Whitney',
            'Whitney / Edwards',
            'Whitney/Trumbull'

                  ],
        'Orange Afternoon':[
            '333 Cedar',
            'Chapel/York',
            'College/Wall (Northbound)',
            '135 Prospect',
            'College/Wall (Southbound)',
            'Phelps Gate',
            'LEPH/60 College',
            'Orange/Humphrey (Southbound)',
            'Willow/Foster',
            'Foster/Edwards',
            'Lot 22 (Whitney/Humphrey)',
            'Canner/Whitney',
            'Orange/Willow (Southbound)',
            'Orange/Canner',
            'Edwards/Orange',
            'Orange/Pearl (Southbound)',
            'Pierson Sage Garage',
            'Congress/Cedar',
            '129 York',
            'SOM (Afternoon)',
            '300 George',
            'Audubon/Orange',
            'College/Crown',
            'Grove/Temple',
            'Grove/Whitney',
            'Whitney / Edwards'

                            ]
}

#stations with LED number on appropiate strip
STATION_LOCATIONS = {
        'Blue Day':[
            ('333 Cedar',0),
            ('Orange/Humphrey (Southbound)',34),
            ('Pierson Sage Garage',58),
            ('Whitney/Cold Spring', 79)
            ],

        'Blue Night':[
            ('333 Cedar',0),
            ('Helen Hadley Hall', 28),
            ('Union Station (Southbound)',64),
            ('81 George St.',79)
],
#        'Green Line':[
#            ],
#
        'Red':[
            ('College/Wall (Northbound)', 0),
            ('Chemistry/225 Prospect (N) /SCL', 22),
            ('CSS',34),
            ('Court/Olive',78),
            ('Winchester/Division',93)

            ],
        'Orange Day':[
            ('333 Cedar', 0),
            ('Orange/Humphrey (Southbound)',26),
            ('Orange/Pearl (Southbound)',52),
            ('Whitney / Edwards',75)

            ],

        'Orange Night':[


            ('333 Cedar', 0),
            ('CSS', 27),
            ('Amistad/CSS',57),
            ('Whitney/Trumbull',75)


            ],

        'Orange Afternoon':[


            ('333 Cedar',0),
            ('LEPH/60 College',22),
            ('Orange/Willow (Southbound)',50),
            ('129 York',64),
            ('Whitney / Edwards',75)

           ]
        }
#five strips for each line/ number of pixels on each strip 
STRIPS = {
        
        #name, (index, length)
         'blue-dayline': (0, 80),
         'redline': (1, 94),
         'orange-dayline':(2,76)
#        'blue-orange-night-afternoonline': (3, 76), 
}
#set color of routes
ROUTE_COLORS = {
        'Blue Day': MapColors.BLUE,
        'Blue Night': MapColors.BLUE,
        'Red': MapColors.RED,
        'Orange Day': MapColors.ORANGE,
        'Orange Night': MapColors.ORANGE,
        'Orange Afternoon': MapColors.ORANGE
}

#I think each color line switch indicates either a transfer or a branch 
ROUTE_SEGMENTS = {

        'Blue Day':[
        ('blue-dayline', 0 , 79 , True)
            ],

        'Blue Night':[
        ('blue-dayline', 0, 79 , True)
            ],
#        'Green Line':[
#            ],
#
        'Red':[
        ('redline',0,93,True)
        ],

        'Orange Day':[
        ('orange-dayline',0,75,True)
            ],

        'Orange Night':[
        ('orange-dayline',0,75,True)
            ],

        'Orange Afternoon':[
        ('orange-dayline',0,75,True)
            ]
        }
