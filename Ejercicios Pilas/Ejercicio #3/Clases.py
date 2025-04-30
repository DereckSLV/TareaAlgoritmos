from os import system
import time
import math

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
        time.sleep(0.5)
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
    
    def numerosBinarios(self, numero):
        if numero == 0:
            print("Binario: 0")
            return

        binarios = Pila()  # Usamos otra pila para guardar los binarios

        while numero > 0:
            residuo = numero % 2
            binarios.agregarNumero(residuo)
            numero = numero // 2

        print("Binario: ", end="")
        actual = binarios.tope
        while actual is not None:
            print(actual.dato, end="")
            actual = actual.siguiente
        print()
        time.sleep(5)
        system('cls')