# siscan

API de Siscan:
[API Rest Siscan 2019](http://157.245.87.38/swagger/)

Para recuperar el token:
```terminal
$ curl -k http://157.245.87.38/api/public/GetToken -X POST -H "Content-Type: application/json" --data "{\"Username\":\"sigcatie\",\"<USUARIO>\":\"<CLAVE>\"}"
```
