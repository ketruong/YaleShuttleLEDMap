import unirest
response = unirest.get("https://transloc-api-1-2.p.mashape.com/segments.json?agencies=yale&callback=call&geo_area=41.3%2C-72.9%7C5000&routes=4000204",
  headers={
      "X-Mashape-Key": "MvVwHz4aP4mshYXZfLEHw1nUjve2p1OWr1sjsnMtX0AuJgR29q",
          "Accept": "application/json"
            }
            )
print response
