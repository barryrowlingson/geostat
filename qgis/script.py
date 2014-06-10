myLayer = iface.mapCanvas().layers()[1]
print myLayer.name()
for f in myLayer.getFeatures():
    print f.geometry().exportToWkt()[:30]
