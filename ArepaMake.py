#!/usr/bin/python3
# -*- coding: utf8 -*-
print("Vamos a preparar arepas")
print("Según la receta necesitamos por cada taza de harina: 1 taza de agua,")
print("1 cucharada de aceite y 1 cucharadita de sal. Entonces:")
print("¿Cuantas tazas de harina PAN usaremos")
harina = float(input())
agua = harina
aceite = harina / 16
sal = aceite / 3
print("entonces siguiendo las proporciones en tazas serían:")
print(str(harina) + " de harina")
print(str(agua) + " de agua")
print(str(aceite) + " de aceite")
print(str(sal) + " de sal")
print("En un bowl, se vierte el agua, la harina y la sal")
bowl = agua + harina + sal
print("Se mezcla hasta que quede uniforme")
print("Se le da a la mezcla forma de disco")
print("Se coloca con el aceite en un budare hasta dorar, retirar y emplatar")
budare = aceite
arepas = budare + bowl
print("como sabemos que por cada kilo de harina salen aproximadamente")
print("20 arepas y un kilo de harina equivale a 8 tazas (datos aproximados de inetrnet)")
print("sabemos que tenemos " + str(arepas) + " tazas de aprepas, lo que")
arepas = harina * 20 / 8
print("equivale a " + str(arepas) + " unidades")
