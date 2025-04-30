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
        
    def eliminarNumero(self):
        """Elimina y retorna el ultimo elemento insertado"""
        if self.tope is None:
            print("Error: Pila vacia!")
            time.sleep(2)
            system('cls')
            return None
        else:
            eliminado = self.tope.dato
            self.tope = self.tope.siguiente # Avanza el tope al siguiente nodo
            print(f"Numero '{eliminado}' eliminado!")
            time.sleep(2)
            system('cls')
    
    def cima(self):
        # Devuelve el ultimo elemento del tope sin eliminarlo
        if self.tope is None:
            print("Error: Pila vacia!")
            time.sleep(2)
            system('cls')
            return None
        else:
            return self.tope.dato

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
            # Se crean listas auxiliares que permitan guardar los datos
            pares = []
            impares = []
            actual = self.tope
            
            # Guardamos los datos segun donde correspondan en cada lista
            while actual is not None:
                if actual.dato % 2 == 0:
                    pares.append(actual.dato)
                else:
                    impares.append(actual.dato)   
                actual = actual.siguiente
            
            # Vaciamos la pila original
            self.tope = None

            # Agregamos los numeros pares a la pila
            for numero in reversed(pares):
                self.agregarNumero(numero)

            for numero in reversed(impares):
                self.agregarNumero(numero)

            print("Pila ordenada correctamente!")