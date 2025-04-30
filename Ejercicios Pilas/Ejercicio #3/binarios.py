"""Diseñar un método “Convbinario” que reciba un entero como parámetro.
La función, usando una pila, deberá mostrar el número en código binario."""
from Clases import Pila
from os import system
import time

pila = Pila()

while True:
    print("       MENU DE OPCIONES")
    opc = int(input("1. Agregar numero\n2. Mostrar Pila binaria\nSeleccione una opcion: "))
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
            if pila.tope is None:
                print("Primero debe ingresar un número.")
                time.sleep(2)
                system('cls')
            else:
                pila.numerosBinarios(pila.tope.dato)  # Convierte el número más reciente
        case _:
            print("Error: Opcion no reconocida")
            time.sleep(2)
            system('cls')