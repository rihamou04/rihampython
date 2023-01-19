"""Actividad 2
El programa debe almacenar los vectores (1, 2, 3) y (-1, 0, 2) en dos listas y
muestre por pantalla su producto escalar.
Nota: ⃗
El siguiente código es cercano a la solución, pero contiene errores. Haciendo
uso del debugger, explica cómo has encontrado la solución y cuál es esta."""


a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(b)):
    product = a[i-1] * b[i-1]
print("El producto de los vectores" + str(a) + "y" + str(b) + "es" + str(product))