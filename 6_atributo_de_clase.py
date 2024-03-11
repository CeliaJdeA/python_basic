"""Definir un atributo de clase num_students e incrementarlo al crear objetos"""

class Estudiante:
    num_estudiantes = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiante.num_estudiantes += 1

est1 = Estudiante ("Carmen",36)
est2 = Estudiante ("Alonso",25)
est3 = Estudiante ("Silvia",15)
est4 = Estudiante ("Lucia",23)

lista = [est1,est2,est3,est4]

for estudiante in lista:
    print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}")

print("Nº total de estudiantes: ", Estudiante.num_estudiantes)
