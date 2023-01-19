"""Actividad 5
El programa debe preguntar al usuario por una frase y una letra, y mostrar por
pantalla el número de veces que aparece la letra en la frase.
El siguiente código es cercano a la solución, pero contiene errores. Haciendo
uso del debugger, explica cómo has encontrado la solución y cuál es esta."""

frase = input ("Introduce una frase: ")
letra = input ("Introduce una letra")
contador = 0
for i in frase :
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s' ." % (letra, contador, frase))