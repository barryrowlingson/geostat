##[BSR scripts]=group
##areas=vector
##scale_factor=number 2
##buffered=output vector

from PyQt4.QtCore import *
from qgis.core import *

from processing.tools import vector
import processing
from processing.core.VectorWriter import VectorWriter

import rootfind
reload(rootfind)

## 2.0 version. 2.2 has .getObject(...) and .features(...)
areas_layer = processing.getobject(areas)
areas_features = processing.getfeatures(areas_layer)

fields = areas_layer.pendingFields().toList()

POLYGON=3
writer = VectorWriter(buffered, None, fields, POLYGON, areas_layer.crs() )

segments=7

inFeat = QgsFeature()
outFeat = QgsFeature()
inGeom = QgsGeometry()
outGeom = QgsGeometry()

for inFeat in areas_features:
    inGeom = QgsGeometry(inFeat.geometry())
    target_area = inGeom.area() * scale_factor
    for i in range(100):
        d = 2**i
        outGeom = inGeom.buffer(float(d), segments)
        if outGeom.area() > target_area:
            break
    def f(x):
        return float(inGeom.buffer(float(x), segments).area() - target_area)
    print "bisect from ",0," to ",float(d)
    result = rootfind.bisect(f, 0.0, float(d), target_area/100.0, 100)
    outGeom = inGeom.buffer(result['x'], segments)
    outFeat.setGeometry(outGeom)
    writer.addFeature(outFeat)
    
del writer


