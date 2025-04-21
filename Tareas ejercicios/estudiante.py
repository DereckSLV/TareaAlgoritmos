class Estudiante:
    def __init__(self, id, nombre, edad, carrera):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    def agregarCalificacion(self, nota):
        if len(self.calificaciones) < 5:
            self.calificaciones.append(nota)
        else:
            print("Ya se han registrado 5 calificaciones.")

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

    def mostrarInfoEst(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")
