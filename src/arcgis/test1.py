import json
from random_location import get_random_location

data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [106.9138433, 47.9185254]
            },
            "properties": {
                "name": "My Point"
            }
        }
    ]
}

for x in range(100):
    location = list(get_random_location())
    location.reverse()
    
    data["features"].append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": location
        }
    })

# Export the feature set to a GeoJSON file
with open("src/arcgis/files/mgl4.geojson", "w") as f:
    f.write(json.dumps(data))
