# Tablero de control de productores - para municipios

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

```terminal
Zoom al mapa desde la lista de municipios
                        {
                            "type": "zoom",
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c"
                        },
```

```terminal
Filtro en lista de municipios por la capa de productores
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

```terminal
Filtro en lista de municipios por la capa de municipios:
                        {
                            "type": "filter",
                            "by": "whereClause",
                            "targetId": "0bc33a5c-1a47-4232-80f5-b6c508bc7b0c#Capa_de_municipios_5083"
                        }
```                        

```terminal
Los dos filtros anteriores:
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
