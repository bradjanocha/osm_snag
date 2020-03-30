#my modules
import os, overpy

api = overpy.Overpass()

#uses the Overpass API's unique query language to 
resultMA = api.query("""area["ISO3166-1"="MA"][admin_level=2];node["place"="city"](area);out;""")
resultDZ = api.query("""area["ISO3166-1"="DZ"][admin_level=2];node["place"="city"](area);out;""")

print("Morocco has " + str(len(resultMA.nodes)) + " cities on OSM while Algeria has " + str(len(resultDZ.nodes)) + ".")