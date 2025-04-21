import time
from os import system
from estudiante import Estudiante

# Lista global de estudiantes
estudiantes = []

def menuOpciones():
    system("cls")  # Limpiar pantalla cada vez que se entra al menú
    opc = int(input(
        "\n------ Menu de Opciones ------"
        "\n1. Registrar nuevo estudiante"
        "\n2. Agregar calificacion a un estudiante"
        "\n3. Mostrar informacion de un estudiante"
        "\n4. Mostrar todos los estudiantes"
        "\n5. Salir del programa"
        "\nSeleccione una opción: "
    ))

    match opc:
        case 1:
            registrarEstudiante()
        case 2:
            agregarNota()
        case 3:
            mostrarEstudiante()
        case 4:
            mostrarTodos()
        case 5:
            print("Saliendo del programa")
            time.sleep(2)
            exit()
        case _:
            print("Opción inválida")
            time.sleep(2)

def registrarEstudiante():
    system("cls")
    print("Registrar nuevo estudiante")
    id = input("Carnet (8 dígitos): ")
    if not validacionCarnet(id):
        return
    nombre = input("Nombre: ")
    if not validacionValoresAlfabeticos(nombre):
        return
    edad = input("Edad: ")
    if not validacionEdad(edad):
        return
    carrera = input("Carrera: ")
    if not validacionValoresAlfabeticos(carrera):
        return

    estudiante = Estudiante(id, nombre, int(edad), carrera)
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito")
    time.sleep(2)

def agregarNota():
    system("cls")
    print("Agregar calificación")
    id = input("Carnet del estudiante: ")
    estudiante = buscarEstudiante(id)
    if estudiante:
        try:
            nota = float(input("Digite la nota (0-100): "))
            if 0 <= nota <= 100:
                estudiante.agregarCalificacion(nota)
                print("Nota registrada con éxito.")
            else:
                print("Nota fuera de rango.")
        except:
            print("Entrada inválida.")
    time.sleep(2)

def mostrarEstudiante():
    system("cls")
    id = input("Carnet del estudiante: ")
    estudiante = buscarEstudiante(id)
    if estudiante:
        estudiante.mostrarInfoEst()
    time.sleep(3)

def mostrarTodos():
    system("cls")
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for est in estudiantes:
            est.mostrarInfoEst()
            print("-" * 30)
    time.sleep(5)

# Validaciones
def validacionCarnet(id):
    if len(id) != 8 or not id.isdigit():
        print("Carnet inválido (debe tener 8 dígitos).")
        time.sleep(2)
        return False
    for est in estudiantes:
        if est.id == id:
            print("Este carnet ya está registrado.")
            time.sleep(2)
            return False
    return True

def validacionEdad(edad):
    if not edad.isdigit() or int(edad) < 16:
        print("Edad inválida (mínimo 16 años)!.")
        time.sleep(2)
        return False
    return True

def validacionValoresAlfabeticos(nombre):
    if not nombre.isalpha():
        print("Introduzca unicamente valores alfabeticos!")
        time.sleep(2)
        system("cls")
        return False
    return True

def buscarEstudiante(id):
    for est in estudiantes:
        if est.id == id:
            return est
    print("Estudiante no encontrado.")
    return None
