#Ejemplificando la creación de una lista enlazada simple

# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
    # Metodo para insertar un valor al inicio de la lista
    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza:
            self.cabeza = nuevo

    # Metodo para medir la longitud de la lista
    def longitudLista(self):
        long = 0
        
        if not self.cabeza:
            return long
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
                long += 1
            
            return long
    
    # Metodo para saber si la lista esta vacia
    def listaVacia(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
    
    # Metodo para encontrar el ultimo valor de la lista
    def ultimoValorLista(self):
        if not self.cabeza:
            return self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            return actual

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
"""Esta línea asegura que el siguiente bloque solo se ejecuta
   si el archivo se corre directamente, y no cuando es importado 
   como módulo en otro archivo"""
if __name__ == "__main__":
    lista = ListaEnlazada()  #Creando el objeto lista

    while True:
        print("Seleccione la opcion a ejecutar")
        print("1. Insertar valor a la lista\n2. Insertar valor al inicio de la lista")
        print("3. Mostrar tamanio de la lista\n4. Mostrar ultimo elemento de la lista")
        opc = int(input("Digite opcion: "))
        match opc:
            case 1:
                valor = int(input("Digite el valor: "))
                lista.insertar(valor)
                
            case 2:
                valor = int(input("Digite el valor: "))
                lista.insertarInicio(valor)

            case 3:
                if lista.longitudLista() == 0:
                    lista.listaVacia()
                else:
                    print(f"Longitud de la lista: ", {lista.longitudLista()})
            case 4:
                print(f"Ultimo valor de la lista: ", {lista.ultimoValorLista()})
            case _:
                print("Opcion invalida, intentelo de nuevo!")
    
    """lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    lista.insertar(40)
    lista.imprimir()  # Lista: 10 -> 20 -> 30 -> 40 -> None
    print("Buscando el valor 20", lista.buscar(20))  # True
    print("Buscar el número 50?", lista.buscar(50))  # False
    lista.eliminar(30)
    lista.imprimir()  # Lista: 10 -> 20 -> 40 -> None
    lista.eliminar(10)
    lista.imprimir()  # Lista: 20 -> 40 -> None
    lista.imprimir()  # Lista: 20 -> 40 -> None"""
