import random

def randomQuickSort(listaDatos, inicio, fin):
    if inicio < fin:
        indicePivote = particionRandom(listaDatos, inicio, fin)
        randomQuickSort(listaDatos, inicio, indicePivote - 1)
        randomQuickSort(listaDatos, indicePivote + 1, fin)

def particionRandom(listaDatos, inicio, fin):
    indiceAleatorio = random.randint(inicio, fin)
    listaDatos[indiceAleatorio], listaDatos[fin] = listaDatos[fin], listaDatos[indiceAleatorio]
    return particion(listaDatos, inicio, fin)

def particion(listaDatos, inicio, fin):
    pivote = listaDatos[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if listaDatos[j] <= pivote:
            i += 1
            listaDatos[i], listaDatos[j] = listaDatos[j], listaDatos[i]
    listaDatos[i + 1], listaDatos[fin] = listaDatos[fin], listaDatos[i + 1]
    return i + 1

try:
    cantidadDatos = int(input("Cuántos números deseas ordenar? "))
    if cantidadDatos <= 0:
        print("Por favor ingresa un número mayor a cero")
    else:
        listaDatos = []
        for i in range(cantidadDatos):
            numero = int(input(f"Ingrese el número {i + 1}: "))
            listaDatos.append(numero)
        print("Lista original:", listaDatos)
        randomQuickSort(listaDatos, 0, len(listaDatos) - 1)
        print("Lista ordenada:", listaDatos)
except ValueError:
    print("Por favor ingresa solo números enteros")
