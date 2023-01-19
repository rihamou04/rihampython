"""El programa debe convertir un número decimal en binario. Otra función,
convertirá un número binario en decimal.
El siguiente código es cercano a la solución, pero contiene errores. Haciendo
uso del debugger, explica cómo has encontrado la solución y cuál es esta"""
def to_decimal(n):
    n = list(n)
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** (len(n) - 1 - i)
    return decimal

def to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    return ''.join(binary)[::-1]

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))