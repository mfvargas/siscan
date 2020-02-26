# Campos adicionales
Las siguientes son las fórmulas de campos adicionales a los que provienenen de los archivos GeoJSON. Deben agregarse en cada _Feature Layer (alojado)_, en la pantalla visualización de la tabla de datos, con la opción _Agregar campo_.

## Capa: Productores
Campo: Valuemunicipio
```terminal
IIf($feature.Keymunicipio==10, 'Ciudad Antigua', 
IIf($feature.Keymunicipio==5, 'Mosonte',
IIf($feature.Keymunicipio==22, 'Totogalpa', 
IIf($feature.Keymunicipio==23, 'Telpaneca', 
IIf($feature.Keymunicipio==25, 'Palacagüina', 
IIf($feature.Keymunicipio==26, 'Yalagüina', 
IIf($feature.Keymunicipio==21, 'Somoto', 
IIf($feature.Keymunicipio==27, 'San Lucas', 
IIf($feature.Keymunicipio==30, 'Pueblo Nuevo', 
IIf($feature.Keymunicipio==31, 'Condega',  
'Otro'
)
)
)
)
)
)
)
)
)
)
```

Campo: Valuetipoobra
```terminal
IIf($feature.Keytipoobra==1, 'Escorrentía', 
IIf($feature.Keytipoobra==2, 'Manantial',
IIf($feature.Keytipoobra==3, 'Techo', 
IIf($feature.Keytipoobra==4, 'Asistencia técnica', 
'Otro'
)
)
)
)
```

Campo: Valuesexo
```terminal
IIf($feature.Keysexo==1, 'Hombre', 
IIf($feature.Keysexo==2, 'Mujer',
'Otro'
)
)
```

Campo: Valueedad
```terminal
IIf($feature.Edad<65, 'Menor de 65', 
IIf($feature.Edad>=65, 'De 65 o más',
'Otro'
)
)
```
