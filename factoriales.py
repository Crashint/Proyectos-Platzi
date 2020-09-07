def factorial(n):
    """ Devuelve el factorial del numero
    n  int > 0"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Escribe un numero entero: '))


print(factorial(n))    