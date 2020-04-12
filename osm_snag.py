#my modules
import os, overpy

api = overpy.Overpass()

print("Enter the ISO code of the country for which you want data:")
country = input()

#uses the Overpass API's unique query language to 
resultMA = api.query(f"""area["ISO3166-1"={country}][admin_level=2];node["place"="city"](area);out;""")
resultDZ = api.query("""area["ISO3166-1"="DZ"][admin_level=2];node["place"="city"](area);out;""")

print("The requested country has " + str(len(resultMA.nodes)) + " cities on OSM while Algeria has " + str(len(resultDZ.nodes)) + ".")