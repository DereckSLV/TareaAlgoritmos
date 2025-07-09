def busquedaSecuencial(listaDatos, objetivo):
    for i in range(len(listaDatos)):
        if listaDatos[i] == objetivo:
            return i  # Devuelve la posición si encuentra el elemento
    return -1  # Devuelve -1 si el elemento no está en el arreglo

try:
    cantidadDatos = int(input("Cuántos números deseas ingresar para la búsqueda? "))
    if cantidadDatos <= 0:
        print("Por favor ingresa un número mayor a cero")
    else:
        listaDatos = []
        for i in range(cantidadDatos):
            numero = int(input(f"Ingrese el número {i + 1}: "))
            listaDatos.append(numero)
        print("Lista ingresada:", listaDatos)
        objetivo = int(input("Qué número deseas buscar? "))
        posicion = busquedaSecuencial(listaDatos, objetivo)
        if posicion != -1:
            print(f"El elemento {objetivo} se encuentra en la posición {posicion}")
        else:
            print(f"El elemento {objetivo} no se encuentra en la lista")
except ValueError:
    print("Por favor ingresa solo números enteros")
