##[BSR scripts]=group
##areas=vector
##owner=field areas
##conflicts=output vector

from PyQt4.QtCore import *
from qgis.core import *

from processing.tools import vector
import processing
from processing.core.VectorWriter import VectorWriter

areas_layer = processing.getobject(areas)
areas_features = processing.getfeatures(areas_layer)
attrid = areas_layer.fieldNameIndex(owner)

fields={}

POLYGON=3
writer = VectorWriter(conflicts, None, fields, POLYGON, areas_layer.crs() )

aFeat = QgsFeature()
bFeat = QgsFeature()
outFeat = QgsFeature()
aGeom = QgsGeometry()
bGeom = QgsGeometry()

all_features = list(areas_features)
n_features = len(all_features)
for ia in range(n_features):
    aFeat = all_features[ia]
    aGeom = QgsGeometry(aFeat.geometry())
    atMapA = aFeat.attributes()[attrid]
    for ib in range(ia+1, n_features):
        bFeat = all_features[ib]
        atMapB = bFeat.attributes()[attrid]
        if atMapA != atMapB:
            bGeom = QgsGeometry(bFeat.geometry())
            if aGeom.intersects(bGeom):
                int_geom = QgsGeometry(aGeom.intersection(bGeom))
                outFeat.setGeometry(int_geom)
                writer.addFeature(outFeat)
    
del writer


