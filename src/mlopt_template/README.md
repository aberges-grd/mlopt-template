### Jerarquía de imports

Como guía general para la estructura del código se establece este orden jerárquico de los imports.

1. Common
2. Data
3. ML
4. Controller

Cada capa puede importar de todas las que tiene por encima, pero no debe importar nada de aquellas que
están por debajo en jerarquía.
