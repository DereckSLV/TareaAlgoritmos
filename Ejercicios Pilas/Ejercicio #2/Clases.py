from os import system
import time

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        
    def agregarNumero(self, dato):
        """Agrega un elemento a la pila """
        nuevoNodo = Nodo(dato) 
        nuevoNodo.siguiente = self.tope # El nuevo nodo apunta al anterior tope
        self.tope = nuevoNodo # El nuevo nodo ahora es el tope

        print(f"Numero '{dato}' agregado!")
        time.sleep(2)
        system('cls')

    def mostrarNumeros(self):
        # Imprime la pila de arriba hacia abajo
        if self.tope is None:
            print("Error: Pila vacia!")
            time.sleep(2)
            system('cls')
            return None
        else:
            print("Contenido de la pila (de arriba hacia abajo)")
            actual = self.tope
            while actual is not None:
                print(actual.dato)
                actual = actual.siguiente
    
    def ordernarNumeros(self):
        if self.tope is None:
            print("Error: Pila vacia!")
            time.sleep(2)
            system('cls')
            return None
        else:
            # Se crean lista auxiliar que permitan guardar los datos
            numeros = []
            actual = self.tope
            
            # Extraemos todos los datos de la pila
            while actual is not None:
                numeros.append(actual.dato)
                actual = actual.siguiente

            # Se ordenan de mayor a menos
            numeros.sort(reverse=True)

            # Vaciamos la pila original
            self.tope = None

            # Agregamos los numeros pares a la pila
            for numero in numeros:
                self.agregarNumero(numero)

            print("Pila ordenada correctamente!")
            time.sleep(2)
            system('cls')