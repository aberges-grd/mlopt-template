# Data layer

La capa de datos debe contener el código necesario para la entrada y salida de datos y transformaciones,
así como la comprobación.

<!-- La transformación usando media/std es impura -->

## Ports

Los puertos modelan el "acceso" a datos.
Las funciones y clases en esta capa se tratan como IO, y por tanto no es código puro.

## Transforms

Las transformaciones de datos deberían ser componibles y puras, de forma que puedan ser 
usadas tanto en combinación con los puertos para escribir datos intermedios, como añadidas
a la entrada de los modelos como parte de un end-to-end (relevante para el despliegue 
de modelos, o entrenamiento dockerizado).

Las transformaciones pueden tener un estado "erróneo", por lo que deberían devolver
Result. 

## Quality (?)

En esta carpeta pueden ir funciones y clases orientadas a reporte y comprobación de
esquemas de datos (por ejemplo con `pandera`).

(en revisión)
