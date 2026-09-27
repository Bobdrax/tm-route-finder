"""
base_conocimiento.py

Guarda la info del sistema (lineas, estaciones y tiempos) como datos,
y con eso arma el grafo que despues usa el buscador de rutas (A*/Dijkstra).
"""

from collections import defaultdict

# ------------------------------------------------------------------
# Datos del sistema
# ------------------------------------------------------------------

LINEAS = {
    "Caracas": [
        "Portal Usme", "Molinos", "Consuelo", "Country Sur", "Quiroga",
        "Olaya", "Restrepo", "Fucha", "Tercer Milenio",
        "Av. Jimenez", "Las Aguas",
    ],
    "Caracas Sur": [
        "Portal Usme", "Molinos", "Consuelo", "Country Sur", "Quiroga",
        "Olaya", "Restrepo", "Fucha", "Tercer Milenio", "Av. Jimenez",
    ],
    "Autonorte": [
        "Portal Norte", "Toberin", "Mazuren", "Alcala", "Prado",
        "Calle 100", "Virrey", "Calle 76", "Calle 72", "Calle 63",
        "Flores", "Calle 45", "Av. Jimenez",
    ],
    "Eje Ambiental": [
        "Av. Jimenez", "Las Aguas",
    ],
    "NQS": [
        "Portal Sur", "Perdomo", "Venecia", "Alqueria", "Sena",
        "Autopista Sur", "NQS Calle 30 Sur", "Comuneros", "Ricaurte",
        "NQS Calle 38A Sur", "Santa Isabel", "NQS Calle 75",
        "Av. Jimenez",
    ],
}

# minutos aproximados entre estaciones seguidas, por linea
TIEMPO_TRAMO = {
    "Caracas": 3,
    "Caracas Sur": 3,
    "Autonorte": 3,
    "Eje Ambiental": 2,
    "NQS": 3,
}

TIEMPO_TRANSBORDO = 5  # penalizacion por cambiar de linea en una estacion


# ------------------------------------------------------------------
# Construccion del grafo
# ------------------------------------------------------------------

def estaciones_por_linea(lineas):
    """Que lineas pasan por cada estacion."""
    por_estacion = defaultdict(set)
    for linea, estaciones in lineas.items():
        for est in estaciones:
            por_estacion[est].add(linea)
    return dict(por_estacion)


def construir_grafo(lineas, tiempos):
    """
    Grafo de adyacencia:
        grafo[estacion] = [(vecino, minutos, linea), ...]

    Se conectan estaciones seguidas de la misma linea (en ambos sentidos).
    El costo de transbordo NO se mete aca: se cobra en la busqueda,
    porque depende de la linea en la que venia el usuario.
    """
    grafo = defaultdict(list)
    for linea, estaciones in lineas.items():
        for i in range(len(estaciones) - 1):
            a, b = estaciones[i], estaciones[i + 1]
            if a == b:
                continue
            t = tiempos[linea]
            grafo[a].append((b, t, linea))
            grafo[b].append((a, t, linea))
    return dict(grafo)


def transbordos(pertenencia):
    """Estaciones donde se puede cambiar de linea."""
    return {
        est: sorted(lineas)
        for est, lineas in pertenencia.items()
        if len(lineas) > 1
    }


def costo_arco(costo, linea_arco, linea_actual):
    """
    Lo que cuesta recorrer un arco.
    Si cambio de linea respecto al tramo anterior, sumo el transbordo.
    """
    if linea_actual is not None and linea_arco != linea_actual:
        return costo + TIEMPO_TRANSBORDO
    return costo


def construir_base():
    pertenencia = estaciones_por_linea(LINEAS)
    grafo = construir_grafo(LINEAS, TIEMPO_TRAMO)
    return grafo, pertenencia, transbordos(pertenencia)


# ------------------------------------------------------------------
# Para probar rapido
# ------------------------------------------------------------------

if __name__ == "__main__":
    grafo, pertenencia, trasb = construir_base()

    print(f"Estaciones: {len(grafo)}")
    print(f"Transbordos: {len(trasb)}")
    print()

    print("Transbordos detectados:")
    for est, lineas in trasb.items():
        print(f"  {est}: {', '.join(lineas)}")

    print()
    print("Vecinos de Av. Jimenez:")
    for vecino, costo, linea in grafo["Av. Jimenez"]:
        print(f"  -> {vecino}  ({costo} min, linea {linea})")
