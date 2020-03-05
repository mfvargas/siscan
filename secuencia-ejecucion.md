# Procesamiento

## Capas geoespaciales
### Descompresión de las capas geoespaciales
```terminal
$ cd datos
$ unzip 2016_INETER_DPA_Municipios.zip
$ unzip 2016_INETER_Internacional_Lin.zip
$ unzip LIM_COM_INETER_2016_Code.zip
$ unzip nomenclator.zip
$ cd ..
```

### Procesamiento de capas de límites político administrativos
```terminal
# Municipios
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 \
-where "muni='Ciudad Antigua' OR muni='Mosonte' OR muni='Totogalpa' OR muni='Telpaneca' OR muni='Palacagüina' OR muni='Yalagüina' OR muni='Somoto' OR muni='San Lucas' OR muni='Pueblo Nuevo' OR muni='Condega'" \
capa-municipios.geojson \
datos/2016_INETER_DPA_Municipios.shp

# Comunidades
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 \
-where "municipio='Ciudad Antigua' OR municipio='Mozonte' OR municipio='Totogalpa' OR municipio='Telpaneca' OR municipio='Palacaguina' OR municipio='Yalaguina' OR municipio='Somoto' OR municipio='San Lucas' OR municipio='Pueblo Nuevo' OR municipio='Condega'" \
capa-municipios.geojson \
datos/LIM_COM_INETER_2016_Code.shp

# Límite nacional
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 \
capa-limite_nicaragua.geojson \
datos/2016_INETER_Internacional_Lin.shp
```
