from buscador_rutas import dijkstra, grafo


print("========================================")
print("     SISTEMA DE RUTAS TRANSMILENIO")
print("========================================")


# Mostrar estaciones disponibles
print()
print("Estaciones disponibles:")
print()

for estacion in sorted(grafo):

    print(f"- {estacion}")


print()


# Solicitar estación de origen
origen = input(
    "Ingrese estación de origen: "
)


# Solicitar estación de destino
destino = input(
    "Ingrese estación de destino: "
)


# Validar estación de origen
if origen not in grafo:

    print()

    print(
        "La estación de origen no existe."
    )

    exit()


# Validar estación de destino
if destino not in grafo:

    print()

    print(
        "La estación de destino no existe."
    )

    exit()


print()
print("Calculando mejor ruta...")
print()


# Ejecutar Dijkstra
resultado = dijkstra(
    grafo,
    origen,
    destino
)


# Mostrar resultado
if resultado:

    ruta, tiempo = resultado

    print("========================================")
    print("           RUTA ENCONTRADA")
    print("========================================")

    print()

    print(
        " -> ".join(ruta)
    )

    print()

    print(
        f"Tiempo total estimado: {tiempo} minutos"
    )

    print()

    print("========================================")


else:

    print()

    print(
        "No se encontró una ruta entre "
        "las estaciones seleccionadas."
    )