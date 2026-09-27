# Sistema Inteligente de Rutas - TransMilenio

Sistema experto que calcula la mejor ruta entre dos estaciones de TransMilenio, a partir de una base de conocimiento escrita como hechos y reglas lógicas, resuelta mediante el algoritmo de búsqueda **Dijkstra**.

## Integrantes

* Johan David Cifuentes Linares — Base de conocimiento (hechos y reglas lógicas)
* Brayan David Gil Barbosa — Motor de búsqueda, interfaz y pruebas

## Estructura del proyecto

```text
base_conocimiento.py   -> Hechos y reglas lógicas: genera el grafo de estaciones/líneas
buscador_rutas.py      -> Implementación del algoritmo de búsqueda Dijkstra
main.py                -> Interfaz de consola para solicitar origen y destino y mostrar la ruta
```

## Requisitos

* Python 3.8 o superior.
* No requiere librerías externas, solamente la librería estándar de Python.

<!-- ============================================================
     SECCIÓN: BASE DE CONOCIMIENTO
     ============================================================ -->

## Base de conocimiento (`base_conocimiento.py`)

### Diseño

* **Hechos**: cada línea troncal se representa como una secuencia ordenada de estaciones mediante el diccionario `LINEAS`.

* **Regla 1 (conexión directa)**: si dos estaciones son consecutivas en una línea, existe un arco entre ellas con un costo en minutos.

* **Regla 2 (transbordo)**: si una estación pertenece a más de una línea, se identifica como una estación de transbordo.

* **Regla 3 (costo de transbordo)**: cuando el recorrido cambia de una línea a otra, se agregan 5 minutos al costo del recorrido.

Estas reglas se aplican sobre los hechos para construir el grafo de adyacencia que utiliza el motor de búsqueda.

### Ejecución independiente (prueba rápida)

```text
python base_conocimiento.py
```

Muestra el total de estaciones, las estaciones de transbordo detectadas y un ejemplo de los vecinos de una estación.

### Ampliar el mapa de estaciones

Para agregar más líneas o estaciones, basta con añadir una nueva entrada en el diccionario `LINEAS` y establecer su tiempo de tramo correspondiente en `TIEMPO_TRAMO` dentro de `base_conocimiento.py`.

<!-- ============================================================
     SECCIÓN: MOTOR DE BÚSQUEDA
     ============================================================ -->

## Motor de búsqueda (`buscador_rutas.py`)

El motor de búsqueda utiliza el algoritmo **Dijkstra** para encontrar una ruta entre una estación de origen y una estación de destino.

El algoritmo utiliza como entrada el grafo generado por `base_conocimiento.py`.

### Funcionamiento del algoritmo

Dijkstra mantiene una cola de prioridad para seleccionar la estación con el menor costo acumulado.

Para cada estación visitada:

1. Se consultan las estaciones vecinas.
2. Se calcula el costo del desplazamiento.
3. Se tiene en cuenta el tiempo del tramo.
4. Si se cambia de línea, se agrega el costo del transbordo.
5. Se compara el nuevo costo con el costo conocido anteriormente.
6. Si la nueva ruta tiene un menor costo, se actualiza la información.
7. Al llegar al destino se reconstruye la ruta desde el destino hasta el origen.

El resultado obtenido contiene:

* La secuencia de estaciones que conforman la ruta.
* El tiempo total estimado del recorrido.

### Ejecución del motor de búsqueda

El algoritmo puede ejecutarse directamente mediante:

```text
python buscador_rutas.py
```

Por ejemplo:

```text
Ruta encontrada:
Portal Norte -> Toberin -> Mazuren -> Alcala -> Prado -> Calle 100 -> Virrey -> Calle 76 -> Calle 72

Tiempo total: 24 minutos
```

<!-- ============================================================
     SECCIÓN: EJECUCIÓN DEL PROGRAMA COMPLETO
     ============================================================ -->

## Ejecución del programa completo

La interfaz principal se encuentra en `main.py`.

Para ejecutar el sistema completo:

```text
python main.py
```

El programa muestra las estaciones disponibles y solicita al usuario:

```text
Ingrese estación de origen:
Ingrese estación de destino:
```

Después de ingresar las dos estaciones, el sistema:

1. Valida que las estaciones existan.
2. Ejecuta el algoritmo Dijkstra.
3. Busca la ruta con menor costo.
4. Muestra la ruta encontrada.
5. Muestra el tiempo total estimado.

### Ejemplo de ejecución

```text
========================================
     SISTEMA DE RUTAS TRANSMILENIO
========================================

Ingrese estación de origen: Portal Norte
Ingrese estación de destino: Calle 72

Calculando mejor ruta...

========================================
           RUTA ENCONTRADA
========================================

Portal Norte -> Toberin -> Mazuren -> Alcala -> Prado -> Calle 100 -> Virrey -> Calle 76 -> Calle 72

Tiempo total estimado: 24 minutos
```

Si el usuario introduce una estación que no existe, el sistema muestra un mensaje indicando que la estación no es válida.

## Pruebas

Se diseñaron y ejecutaron casos de prueba para verificar el funcionamiento del algoritmo de búsqueda y de la interfaz de consola.

Las pruebas contemplan diferentes situaciones:

* Búsqueda de una ruta entre estaciones válidas.
* Búsqueda de rutas entre diferentes sectores.
* Búsqueda de una ruta que requiere transbordo.
* Ingreso de una estación inexistente.

Los resultados de las pruebas y las capturas de pantalla se encuentran documentados en el PDF de pruebas del proyecto.
