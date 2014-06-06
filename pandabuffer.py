
cdict = {'red': ((0.0,1.0,1.0),(1.0,1.0,1.0)), 'green': ((0.0,1.0,1.0),(1.0,1.0,1.0)), 'blue': ((0.0,1.0,1.0),(1.0,1.0,1.0))}

my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,5)



# read england from shapefile

import geopandas as gpd

england = gpd.read_file("./data/England/engos.shp")

## bufs = [areabuffer.abuff(p, float(p.area*2), 100000, 100000)['geometry'] for p in england['geometry']]

bufs = gpd.GeoSeries([areabuffer.abuff(p, float(p.area*2), 100000, 100000)['geometry'] for p in england.geometry])

bufs[5:6].plot()

england[5:6].plot()

