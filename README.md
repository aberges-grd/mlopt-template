# Plantilla para proyectos de la línea ML&Opt

Esta plantilla tiene por objetivo ayudar a los nuevos desarrolladores a tener un código
estructurado [...]

# Herramientas

La plantilla usa [`pdm`][pdm], un gestor de paquetes similar a `poetry`. Para instalarlo,
se recomienda la manera oficial, con el comando:

```bash
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
``` 

o, en Windows:

```powershell
(Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | py -
```

Una vez instalado, podemos usar `pdm install` para instalar las dependencias listadas en el archivo
`pyproject.toml`. Las que vienen por defecto son:

- pytest: el estándar _de facto_ para escribir tests en Python.
- [`attrs`][attrs]: librería similar a `dataclasses` para agilizar la programación.
- [`returns`][returns]: trae ciertos aspectos de programación funcional a Python, facilitando gestión de excepciones.
- [`typer`][typer]: permite crear interfaces de línea de comandos muy fácilmente.
- [`rich`][rich]: ayuda con el formateo de texto por pantalla, entre otras cosas tiene "pretty print" de estructuras
  como diccionarios o formato enriquecido para los logs. 

Estas librerías se consideran una base sobre la que desarrollar. No son específicas de ML, sino de desarrollo de software
en general.

Otra herramienta que se considera fundamental es [Docker][docker], ya que en la medida de lo posible los entrenamientos
deberían ser hechos en contenedores. 

# Librerías

La plantilla, irónicamente, no impone librerías de ML o DS. No obstante, se sugieren algunas a continuación.
Para usar cualquiera de ellas con PDM, lanza el comando:

```
pdm add <nombrelibrería>
```

**Procesado de datos**

- [pola.rs][polars]: librería similar a pandas en funcionalidad pero usualmente más rápida, con distinta sintaxis.
- [dask][dask]: recomendado para grandes volúmenes de datos (1Tb o más, que requiera computación distribuída).

**Gráficos**

- matplotlib.
- altair (recomendable también instalar vega-fusion).

**Machine learning**

- scikit-learn
- Pytorch o Tensorflow
- XGBoost

[pdm]: <https://pdm-project.org/en/latest/>
[attrs]: <https://www.attrs.org/en/stable/index.html>
[returns]: <https://returns.readthedocs.io/en/latest/index.html>
[typer]: <https://typer.tiangolo.com/>
[rich]: <https://rich.readthedocs.io/en/latest/>
[docker]: <https://www.docker.com/>
[polars]: <https://pola.rs/>
[dask]: <https://www.dask.org>
