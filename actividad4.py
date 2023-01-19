"""Actividad 4
Escribir un programa que almacene la cadena de caracteres 12345EDD como
contraseña. En una variable, pregunte al usuario por la contraseña hasta que
introduzca la contraseña correcta."""

code="12345EDD"
contraseña = ""
while contraseña != code:
    contraseña =input("Introduce la contraseña")

print('contraseña correcta')