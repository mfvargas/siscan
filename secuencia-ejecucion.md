Procesamiento de capas de límites político administrativos
```terminal
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 capa-municipios.geojson datos/2016_INETER_DPA_Municipios.shp
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 capa-comunidades.geojson datos/LIM_COM_INETER_2016_Code.shp
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 capa-limite_nicaragua.geojson datos/2016_INETER_Internacional_Lin.shp
```
