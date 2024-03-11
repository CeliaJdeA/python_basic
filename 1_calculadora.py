"""Calculadora con 4 metodos y parametros con decimales"""

def suma(valor1, valor2):
    j = valor1 + valor2
    print('El resultado de la suma suma es ', j, type(j))
def resta(valor1, valor2):
    j = valor1 - valor2
    print('El resultado de la resta es ', j, type(j),j)
def multiplicacion(valor1, valor2):
    j = valor1 * valor2
    print('El resultado de la multiplicación es ', j, type(j),j)
def division(valor1, valor2):
    j = valor1 / valor2
    print('El resultado de la división es ', j, type(j),j)
def switch_case(opcion):
    if opcion == 1:
        print("Opción 1 seleccionada")
        suma(valor1, valor2)
    elif opcion == 2:
        print("Opción 2 seleccionada")
        resta(valor1, valor2)
    elif opcion == 3:
        print("Opción 3 seleccionada")
        multiplicacion(valor1, valor2)
    elif opcion == 4:
        print("Opción 4 seleccionada")
        division(valor1, valor2)
    else:
        print("Opcion no valida")


valor1 = int(input('Inserte un valor entero: '))
valor2 = int(input('Inserte otro valor entero: '))

print('1. SUMA')
print('2. RESTA')
print('3. MULTIPLICACION')
print('4. DIVISION')
opcion = int(input('Introduce el nº de la operacion que quieres realizar: '))
switch_case(opcion)


