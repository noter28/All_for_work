import googlemaps
import json
from pprint import pprint
def loc():
    gmaps = googlemaps.Client(key='googleApikey')

# Geocoding an address
    geocode_result = gmaps.geocode('520 Highway 119 Alabaster, AL 35007')
    a=geocode_result
#    print(a)
    return(a)
loc()
# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
b=json.dumps(loc())
#pprint(b)
n=json.loads(b)
a=(n[0])
#pprint(a)
print(a['geometry']['location'])
# pprint(n['address_components'][0])

