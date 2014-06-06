from shapely.geometry import mapping, shape

import fiona
import sys

def bufferinout(input_shp, output_shp, width):
    with fiona.open(input_shp, "r") as input:
        schema = { 'geometry': 'Polygon', 'properties': { 'name': 'str' } }
        with fiona.open(output_shp, "w", "ESRI Shapefile", schema, crs = input.crs) as output:
            for feature in input:
                output.write({
                'properties': {
                    'name': feature['properties']['ADMIN_NAME']
                },
                'geometry': mapping(shape(feature['geometry']).buffer(width))
                })

if __name__=="__main__":
  input = sys.argv[1]
  output = sys.argv[2]
  width = float(sys.argv[3])
  bufferinout(input, output, width)
  
