"""Escritura en fichero
¿Cómo haría para escribir en fichero en el disco duro?"""

with open('ejemplo.txt', 'w') as archivo:
   # Escribe líneas en el archivo
   archivo.write('Este es un ejemplo de cómo escribir en un archivo en Python.\n')
   archivo.write('Puedes escribir múltiples líneas también.\n')
   archivo.write('¡Es muy útil para guardar datos o resultados!\n')
