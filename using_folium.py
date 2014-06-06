open("niger.json","w").write(niger.to_json())

map_osm = folium.Map(location=[17,10])

map_osm.geo_json(geo_str=niger.to_json(), data=niger, columns=['ADM2','POP'], key_on='feature.properties.ADM2', fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,legend_name="Fake Population")

map_osm.create_map("niger.html")

### mplleaflet

import mplleaflet
niger.plot()
mplleaflet.show()
