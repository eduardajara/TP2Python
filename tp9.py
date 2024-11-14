def ler_num():
    numeros = []
    while True:
        numero = int(input('Digite um numero (0 para encerrar): '))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def invertido(numeros):
    print('Numeros invertidos:')
    for numero in reversed(numeros):
        print(numero)

numeros = ler_num()
invertido(numeros)
