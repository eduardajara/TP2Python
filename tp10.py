def ler():
    numeros = []
    while True:
        numero = int(input('Digite um numero (0 para parar): '))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def resultado(numeros):
    if len(numeros) == 0:
        print('Nenhum numero foi inserido')
        return
    media = sum(numeros) / len(numeros)
    print(f'Média: {media}')
    print('Numeros maiores ou iguais a média:')
    for numero in numeros:
        if numero >= media:
            print(numero)

numeros = ler()
resultado(numeros)
