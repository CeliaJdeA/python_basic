"""Definir una clase estudiante, crear varios estudiantes y meterlos en una lista"""

class Estudiante:
    #nombre = 'Por defecto'
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


est1 = Estudiante ("Carmen",36)
est2 = Estudiante ("Alonso",25)
est3 = Estudiante ("Silvia",15)
est4 = Estudiante ("Lucia",23)

lista = [est1,est2,est3,est4]

for estudiante in lista:
    print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}")

"""Las cadenas de formato (f-strings) te permiten insertar valores de variables o expresiones directamente dentro de 
una cadena de una manera más legible y conveniente. Puedes colocar las variables o expresiones entre llaves {} dentro 
de la cadena, y Python las reemplazará con sus valores reales cuando se evalúe la cadena."""