"""str (string) en Python es inmutable ¿cómo puedo comprobar esto en un pequeño programa?"""

nombre = input("Ingresa tu nombre")
print('cad1 = Hola')
print('cad2 = el nombre ingresado')
print('cad3 = concatenacion de los dos str')
cad1 = 'Hola'
cad2 = nombre
cad3 = cad1 + cad2

print('id cad1: ', id(cad1))
print('id cad2: ', id(cad2))
print('La nueva cadena (',cad3, ') crea un nuevo id de la cad3: ', id(cad3))