def fibonacci(n):
    fib = [0,1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def pertence_fibonnaci(numero):
    fib_sequencia = fibonacci(numero)
    if numero in fib_sequencia:
        print(f'O número {numero} pertence à sequência de Fibonnaci.')
    else:
        print(f'O número {numero} NÃO pertence à sequência de Fibonnaci.')

numero = int(input('Informe um número: '))
pertence_fibonnaci(numero)
