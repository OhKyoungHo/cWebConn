import folium

map_osm = folium.Map(location=[37.572807,126.975918], zoom_start=17 ) # 16~19
#  tiles='Stamen Toner'
folium.Marker(location=[37.572807,126.975918], popup='세종문화회관', icon=folium.Icon(color='red', icon='info-sign')
              ).add_to(map_osm)
map_osm.save('./map/map6.html')