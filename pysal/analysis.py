#
#
# duplicate something from ASDAR using pysal
#


import pysal
import geopandas as gpd
import numpy as np

shapefile = "NY8_utm18.shp"

spdf = gpd.read_file(shapefile)

y = np.array(spdf['Cases'])
w = pysal.open("NY_nb.gal").read()
# w = pysal.queen_from_shapefile(shapefile)
w.histogram
lm = pysal.Moran_Local(y,w,transformation="D")
lmV = pysal.Moran_Local(y,w,transformation="V")


""" 
### R version
NY8 = readOGR(".","NY8_utm18")
# NY_nb = poly2nb(NY8)
NY_nb = read.gal("NY_nb.gal", region.id=row.names(NY8@data))
summary(NY_nb)
lm = localmoran(NY8$Cases, listw = nb2listw(NY_nb, style="C"))
lmV = localmoran(NY8$Cases, listw = nb2listw(NY_nb, style="S"))

"""

"""

### Rpy version

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
spdep = importr("spdep")
NY_nb = spdep.read_gal("./data/NewYork/NY_nb.gal", region=range(281))
lmR = spdep.localmoran(robjects.FloatVector(spdf['Cases']), listw = spdep.nb2listw(NY_nb, style="S"))
plt.hist(lmR.rx(True,"Z.Ii"))
plt.show()
"""
