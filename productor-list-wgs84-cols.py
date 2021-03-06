import pyproj
import csv


archivo_entrada = open('siscan-api-productor-list.csv', 'r', encoding='utf-8')
archivo_salida  = open('productor-list-wgs84-cols.csv', 'w', newline='', encoding='utf-8')

lector_lineas   = csv.reader(archivo_entrada)
escritor_lineas = csv.writer(archivo_salida, delimiter=',')

p1 = pyproj.Proj(init='epsg:32616')
p2 = pyproj.Proj(init='epsg:4326')

pos_col_input_x = 8
pos_col_input_y = 9

min_x = 400000
max_x = 1000000
min_y = 1100000
max_y = 1700000


i = 1
for linea in lector_lineas :
    x1 = linea[pos_col_input_x]
    y1 = linea[pos_col_input_y]
    
    linea_salida = linea
    if i == 1:
        # Línea de encabezado
        linea_salida.append("coord_x")
        linea_salida.append("coord_y")    
        escritor_lineas.writerow(linea_salida)
    elif (x1 != "" and y1 != ""):
        x1 = float(x1)
        y1 = float(y1)
        # if (min_x <= x1 <= max_x) and (min_y <= y1 <= max_y):
            # Caso en el que todo va bien con los datos
        x2, y2 = pyproj.transform(p1, p2, x1, y1)
        linea_salida.append(x2)
        linea_salida.append(y2)
        escritor_lineas.writerow(linea_salida)
        print(i, x1, y1, x2, y2)            
        # else:
            # Caso en el que los valores se salen de los rangos de la proyección de entrada
            # En el caso de Siscan, hay valores de WGS84 en las columnas de UTM 16N
            # y, en algunos casos, los valores de x, y están invertidos
        #    pass

    else:
        # Caso en el que el valor de entrada de x o de y están vacíos
        pass
        
    i += 1


# Cierre de archivos
archivo_entrada.close()
archivo_salida.close()
