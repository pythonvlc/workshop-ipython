def factorial(n):
    if n == 0:
        return 1
    else:
        recursivo = factorial(n - 1)
        resultado = n * recursivo
        return resultado