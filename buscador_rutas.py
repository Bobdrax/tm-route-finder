from base_conocimiento import construir_base, costo_arco
import heapq


# Construimos la base de conocimiento
grafo, pertenencia, transbordos = construir_base()


def dijkstra(grafo, origen, destino):

    # Distancia mínima conocida para cada estación
    distancias = {
        origen: 0
    }

    # Guarda de dónde venimos para reconstruir la ruta
    anteriores = {
        origen: None
    }

    # Cola de prioridad
    #
    # (costo acumulado, estación actual, línea actual)
    cola = [
        (0, origen, None)
    ]

    heapq.heapify(cola)

    while cola:

        costo_actual, actual, linea_actual = heapq.heappop(cola)

        # Si llegamos al destino terminamos
        if actual == destino:
            break

        # Revisamos los vecinos de la estación actual
        for vecino, tiempo, linea in grafo[actual]:

            # Calculamos el costo teniendo en cuenta
            # un posible transbordo
            costo = costo_arco(
                tiempo,
                linea,
                linea_actual
            )

            nuevo_costo = costo_actual + costo

            # Si encontramos una ruta más económica
            if (
                vecino not in distancias
                or nuevo_costo < distancias[vecino]
            ):

                distancias[vecino] = nuevo_costo

                anteriores[vecino] = actual

                heapq.heappush(
                    cola,
                    (
                        nuevo_costo,
                        vecino,
                        linea
                    )
                )

    # Si no llegamos al destino
    if destino not in distancias:

        return None

    # Reconstruimos la ruta
    ruta = []

    actual = destino

    while actual is not None:

        ruta.append(actual)

        actual = anteriores[actual]

    # La ruta se construyó al revés
    ruta.reverse()

    return ruta, distancias[destino]


# Prueba directa del algoritmo
if __name__ == "__main__":

    origen = "Portal Norte"

    destino = "Calle 72"

    resultado = dijkstra(
        grafo,
        origen,
        destino
    )

    if resultado:

        ruta, tiempo = resultado

        print("Ruta encontrada:")

        print(
            " -> ".join(ruta)
        )

        print(
            f"Tiempo total: {tiempo} minutos"
        )

    else:

        print(
            "No se encontró una ruta."
        )