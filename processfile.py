from shapely.geometry import mapping, shape

import fiona

input_shp = "./data/England/engos.shp"
output_shp = "./data/England/buffered.shp"
width = 10000

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

bufferinout(input_shp, output_shp, width)

