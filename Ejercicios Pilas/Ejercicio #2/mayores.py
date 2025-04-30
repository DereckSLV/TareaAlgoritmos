"""Implementa un método llamado “ordena” que reciba una pila de enteros como parámetro
y devuelva la pila ordenada de mayor (fondo de la pila) a menor (top de la pila)."""
from Clases import Pila
from os import system
import time

pila = Pila()

while True:
    print("       MENU DE OPCIONES")
    opc = int(input("1. Agregar numero\n2. Mostrar Pila \n3. Ordenar Pila\nSeleccione una opcion: "))
    match opc:
        case 1:
            numero = int(input("Digite un numero: "))
            if not isinstance(numero, int):
                print("Error: No se permiten caracteres no numericos")
                time.sleep(2)
                system('cls')
            else:
                pila.agregarNumero(numero)
        case 2:
            pila.mostrarNumeros()
        case 3:
            pila.ordernarNumeros()
        case _:
            print("Error: Opcion no reconocida")
            time.sleep(2)
            system('cls')