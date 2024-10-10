# Data layer

La capa de datos debe contener el código necesario para la entrada y salida de datos y transformaciones,
así como la comprobación.

<!-- La transformación usando media/std es impura -->

## Reader/Writer

Los lectores o escritores modelan el acceso a datos y son la parte más externa (en el sentido de interactuar
con otros sistemas) de la capa de datos. Dictan el "cómo" se accede a los datos.

Muchas veces, estos "reader" vienen de otras librerías (p.ej. los distintos métodos que tiene _pandas_).
Los métodos de acceso a datos por su propia naturaleza son "impuros", es decir, lidian con el sistema operativo
y sistemas externos que pueden tener disponibilidad aleatoria (desde el punto de vista de nuestro programa).

Se recomienda por tanto decorar la función lectura/escritura con [`impure_safe`][impure_safe_docs] 
de _returns_. Por ejemplo:

```python
from returns.io import impure_safe

csv_reader = impure_safe(pd.read_csv)
```

O, si estamos definiendo nuestra propia función de acceso:

```python
@impure_safe
def my_data_reader(*args):
    ...
```

Esto transformará la función a una función que devuelve `IOResult`, un tipo que representa este tipo de operaciones
de I/O que pueden fallar (por ejemplo, cualquier excepción será capturada y devuelta en un objeto `Failure`).

[impure_safe_docs]: <https://returns.readthedocs.io/en/latest/pages/io.html#impure-safe>

## Repositories

Los repositorios son "formas concretas" de los datos (por ejemplo: datos de cordones, datos de máquinas, etc). Son instancias
de _readers_ o _writers_.

Los repositorios pueden ser importados por otras partes del código.

Los repositorios deben saber dónde buscar los datos que leen. Las clases o funciones que usen los
repositorios solo tienen que llamar a métodos sin argumentos, no deben saber los detalles de dónde existen esos datos o
cómo se leen.

Un ejemplo de repositorio para datos de sensores que serán leídos de un Excel local, con la opción `parse_dates=True`:

```python
datos_sensores_repo = partial(pd.read_excel, path_or_buf="/path/to/data", parse_dates=True)
```

Posteriormente, el código de ML sólo tendrá que llamar `datos_sensores_repo()` para obtener los datos. Así, si en el
futuro el acceso a esos datos se realiza mediante una BBDD o un Excel en otra ruta, no habrá que modificar el código
de ML.

## Transforms

Las transformaciones de datos deberían ser componibles y puras, de forma que puedan ser  usadas tanto en combinación con
los repositorios para escribir datos intermedios, como añadidas a la entrada de los modelos como parte de un end-to-end
(relevante para el despliegue  de modelos, o para un entrenamiento dockerizado).

Las transformaciones pueden tener un estado "erróneo", por lo que deberían devolver Result.

¿Pueden definirse transformaciones en la capa ML? Por lo general, mejor en data. Si se decide poner en la de ML, se
debe tener en cuenta que en el momento en el que en la capa de datos se haga un `import` de una función en la capa ML,
automáticamente la decisión de diseño se califica como "mala". Si se es capaz de respetar eso, no hay problema.

## Quality

Finalmente, un cuarto módulo de esta capa puede ser el orientado a comprobaciones de la calidad del dato. En este módulo
pueden ir funciones y clases orientadas a reporte y comprobación de esquemas de datos (por ejemplo con `pandera`).
