"""El programa debe almacenar las matrices en una lista y mostrar por pantalla su
producto.
Nota: Para representar matrices mediante listas usar listas anidadas,
representando cada vector fila en una lista.
El siguiente código es cercano a la solución, pero contiene errores. Haciendo
uso del debugger, explica cómo has encontrado la solución y cuál es esta."""

a= ((1,2,3),
    (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
           [0,0]]
for i in range (len(a)):
    for j in range (len(b[0])):
        for k in range(len(b)):
            result[i] [j] += a[i][k] * b[k][j]
for i in range (len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])