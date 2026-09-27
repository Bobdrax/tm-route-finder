# Sistema Inteligente de Rutas - TransMilenio

Sistema experto que calcula la mejor ruta entre dos estaciones de
TransMilenio, a partir de una base de conocimiento escrita como
hechos y reglas lógicas, resuelta con el algoritmo de búsqueda
heurística **A\***.

## Integrantes
- Johan David Cifuentes Linares — Base de conocimiento (hechos y reglas lógicas)
- Brayan David Gil Barbosa — Motor de búsqueda, interfaz y pruebas

## Estructura del proyecto

```
base_conocimiento.py   -> Hechos y reglas lógicas: genera el grafo de estaciones/líneas
motor_busqueda.py       -> (pendiente por agregar)
main.py                 -> (pendiente por agregar)
```

## Requisitos

- Python 3.8 o superior (no requiere librerías externas, solo la
  librería estándar).

<!-- ============================================================
     SECCIÓN: BASE DE CONOCIMIENTO (parte de [Nombre 1])
     ============================================================ -->

## Base de conocimiento (`base_conocimiento.py`)

### Diseño

- **Hechos**: cada línea troncal se representa como una secuencia
  ordenada de estaciones (diccionario `LINEAS`).
- **Regla 1 (conexión directa)**: si dos estaciones son consecutivas
  en una línea, existe un arco entre ellas con un costo en minutos.
- **Regla 2 (transbordo)**: si una estación pertenece a más de una
  línea, se marca como nodo de transbordo.
- Estas reglas se aplican sobre los hechos para construir el grafo
  de adyacencia que consume el motor de búsqueda.

### Ejecución independiente (prueba rápida)

```
python base_conocimiento.py
```

Muestra el total de estaciones, las estaciones de transbordo
detectadas y un ejemplo de vecinos de una estación.

### Ampliar el mapa de estaciones

Para agregar más líneas o estaciones, basta con añadir una nueva
entrada en el diccionario `LINEAS` (y su tiempo de tramo en
`TIEMPO_TRAMO`) dentro de `base_conocimiento.py`.

<!-- ============================================================
     SECCIÓN: MOTOR DE BÚSQUEDA (parte de [Nombre 2])
     [Nombre 2] agrega aquí la explicación del algoritmo A*,
     la heurística usada, y cómo se ejecuta motor_busqueda.py
     ============================================================ -->

## Motor de búsqueda (`motor_busqueda.py`)

_(pendiente — completar por Brayan David Gil Barbosa)_

<!-- ============================================================
     SECCIÓN: EJECUCIÓN DEL PROGRAMA COMPLETO (parte de Brayan David Gil Barbosa)
     Brayan David Gil Barbosa agrega aquí las instrucciones de main.py
     ============================================================ -->

## Ejecución del programa completo

_(pendiente — completar por Brayan David Gil Barbosa)_
