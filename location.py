import googlemaps
import json
from pprint import pprint
def loc():
    gmaps = googlemaps.Client(key='AIzaSyAv44kmc0VxYNSCh8CgZsEYPNnDEph8o3k')

# Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    a=geocode_result
    return(a)
loc()
# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
b=json.dumps(loc())
n=json.loads(b)
pprint(n)
pprint(n['address_components'][0])

