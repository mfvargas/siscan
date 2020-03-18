# Tablero de control de productores - para municipios ("id": "10327b2d320d4a0b8e950e19ec546d67")

## ID de objetos
Mapa
```terminal
0bc33a5c-1a47-4232-80f5-b6c508bc7b0c
```

Capa de productores
```terminal
0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_productores_4637
```

Capa de municipios
```terminal
0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_municipios_5083
```

## Filtros
Zoom al mapa desde la lista de municipios
```terminal
                        {
                            "type": "zoom",
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c"
                        },
```

Filtro en lista de municipios por la capa de productores
```terminal
                        {
                            "type": "filter",
                            "by": "whereClause",
                            "fieldMap": [
                                {
                                    "sourceName": "muni",
                                    "targetName": "Municipio"
                                }
                            ],
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_productores_4637"
                        }
```                        

Filtro en lista de municipios por la capa de municipios
```terminal
                        {
                            "type": "filter",
                            "by": "whereClause",
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_municipios_5083"
                        }
```                        

Los dos filtros anteriores
```terminal
                        {
                            "type": "filter",
                            "by": "whereClause",
                            "fieldMap": [
                                {
                                    "sourceName": "muni",
                                    "targetName": "Municipio"
                                }
                            ],
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_productores_4637"
                        },
                        {
                            "type": "filter",
                            "by": "whereClause",
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_municipios_5083"
                        }  
```
