# Procesamiento

## Importación de capas a ArcGIS Online

### Capas en formatos geoespaciales
#### Descompresión
```terminal
$ cd datos
$ unzip 2016_INETER_DPA_Municipios.zip
$ unzip 2016_INETER_Internacional_Lin.zip
$ unzip LIM_COM_INETER_2016_Code.zip
$ cd ..
```

#### Filtrado y conversión al formato GEOJSON
```terminal
# Municipios
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 \
-where "muni='Ciudad Antigua' OR muni='Mosonte' OR muni='Totogalpa' OR muni='Telpaneca' OR muni='Palacagüina' OR muni='Yalagüina' OR muni='Somoto' OR muni='San Lucas' OR muni='Pueblo Nuevo' OR muni='Condega'" \
capa-municipios.geojson \
datos/2016_INETER_DPA_Municipios.shp

# Comunidades
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 \
-where "municipio='Ciudad Antigua' OR municipio='Mozonte' OR municipio='Totogalpa' OR municipio='Telpaneca' OR municipio='Palacaguina' OR municipio='Yalaguina' OR municipio='Somoto' OR municipio='San Lucas' OR municipio='Pueblo Nuevo' OR municipio='Condega'" \
capa-comunidades.geojson \
datos/LIM_COM_INETER_2016_Code.shp

# Límite internacional
# El archivo suministrado por la coordinación del proyecto (2016_INETER_Internacional_Lin.shp) presentó problemas al momento de subirse a ArcGIS Online, por lo que se utilizó el disponible en https://gadm.org
$ ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 \
capa-limite_nicaragua.geojson \
datos/gadm36_NIC_0.shp
```
Las tres capas se almacenaron como capas alojadas en ArcGIS Online.

### Datos de productores
1. Se descargan los datos del API de Siscan con el comando:
```terminal
$ python siscan-api-productor-list.py
```
(**DEBE ASIGNARSE EL VALOR DEL TOKEN DEL API EN LA VARIABLE CORRESPONDIENTE DEL SCRIPT**)

2. El archivo JSON resultante (```siscan-api-productor-list.json```) se procesa en el sitio [http://www.convertcsv.com/json-to-csv.htm](http://www.convertcsv.com/json-to-csv.htm) desde donde se genera el archivo CSV ```siscan-api-productor-list.csv``` (**DEBE HABILITARSE LA OPCIÓN _Suppress Line Breaks in Fields_**)
3. Se generan las columnas con coordenadas WGS84:
```terminal
$ python productor-list-wgs84-cols.py
```
4. El archivo CSV resultante (```productor-list-wgs84-cols.csv```) fue convertido al formato GeoJSON, con el sistema de información geográfica de escritorio QGIS.
5. El archivo GEOJSON resultante (```capa-productores.geojson```) se almacenó como una capa alojada en ArcGIS Online.

### Datos de obras
1. Se descargan los datos del API de Siscan con el comando:
```terminal
$ python siscan-api-obra-list.py
```
(**DEBE ASIGNARSE EL VALOR DEL TOKEN DEL API EN LA VARIABLE CORRESPONDIENTE DEL SCRIPT**)

2. El archivo JSON resultante (```siscan-api-obra-list.json```) se procesa en el sitio [http://www.convertcsv.com/json-to-csv.htm](http://www.convertcsv.com/json-to-csv.htm) desde donde se genera el archivo CSV ```siscan-api-obra-list.csv``` (**DEBE HABILITARSE LA OPCIÓN _Suppress Line Breaks in Fields_**)
3. Se generan las columnas con coordenadas WGS84:
```terminal
$ python obra-list-wgs84-cols.py
```
4. El archivo CSV resultante (```obra-list-wgs84-cols.csv```) fue convertido al formato GeoJSON, con el sistema de información geográfica de escritorio QGIS.
5. El archivo GEOJSON resultante (```capa-obras.geojson```) se almacenó como una capa alojada en ArcGIS Online.

## Campos adicionales
Deben agregarse los campos que se especifican en [https://github.com/mfvargas/siscan/blob/master/campos-adicionales.md](https://github.com/mfvargas/siscan/blob/master/campos-adicionales.md).
