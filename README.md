# cp_validator

*Códigos Postales Españoles*

Este programa es un ejercicio práctico de **REST** `API` basado en [Flask](http://flask.pocoo.org/) para  validación y consulta de __*Códigos Postales españoles*__.

Los ficheros fuente **de muestra** están publicados por **Correos España** en la [url](http://www.correos.es/ss/Satellite/site/servicio-bd_codigos_postales-marketing_directo_soluciones_empresariales/detalle_servicio-sidioma=es_ES).

:warning: **IMPORTANTE** :warning::  la `BD` completa es **privativa y de pago** :broken_heart:. Su uso exige la suscripción un [contrato](http://www.correos.es/ss/Satellite/site/aplicacion-1349169614869-1363189730359/detalle_app-sidioma=es_ES).

## Instalación


## Métodos

Toda la información se recibe como **JSON**.

[/codigos](#codigos)

[/codigos/{codigo}](#codigo)


### <a name="codigos"></a>Códigos

Devuelve todos los códigos postales

### <a name="codigo"></a>Código

Devuelve los datos específicos para un código concreto.

```bash
$ curl -i http://127.0.0.1:5000/cp/api/v1.0/codigos/29190
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 666
Server: Werkzeug/0.11.13 Python/3.5.2
Date: Fri, 30 Dec 2016 17:53:15 GMT

{
  "29190": {
    "data": [
      {
        "cod_ine": "0000000000000000",
        "cod_localidad": "2900",
        "cod_municipio": "00000",
        "estado": "",
        "id_registro": "29009484",
        "impar_inferior": "0001",
        "impar_superior": "9999",
        "inf_impar_inferior": null,
        "inf_impar_superior": null,
        "inf_par_inferior": null,
        "inf_par_superior": null,
        "localidad": "SIN_DATOS",
        "nombre_via": "AGAPANTO",
        "par_inferior": "0002",
        "par_superior": "9998",
        "tipo_via": "CALLE"
      }
    ],
    "uri": "http://127.0.0.1:5000/cp/api/v1.0/codigos/29190"
  }
}
```

