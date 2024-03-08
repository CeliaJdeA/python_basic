""" Calculadora con 4 metodos y parametros con enteros.
    Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos"""

print('Calculadora con 4 metodos y parametros con enteros')

def suma(x, y):
    j = x + y
    print(type(j),j)
def resta(x, y):
    j = x - y
    print(type(j),j)
def multiplicacion(x, y):
    j = x * y
    print(type(j),j)
def division(x, y):
    j = x / y
    print(type(j),j)

suma(4,1)