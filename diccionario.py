"""Crear dos diccionarios y unirlos"""

dic1 = {"zanahora":"naranja", "manzana":"roja", "pera":"verde"}
dic2 = {"Pepe": 36, "Laura": 15, "Sebas":56, "Claudia":26}

dic_nuevo = {}

for key, value in dic1.items():
    dic_nuevo[key] = value

for key, value in dic2.items():
    dic_nuevo[key] = value

print(dic_nuevo)
