def ler():
    while True:
        numero = int(input('Insira um numero maior ou igual a zero: '))
        if numero >= 0:
            return numero
        else:
            print('Erro: O numero deve ser maior ou igual a zero')

numero_valido = ler()
print('numero valido inserido:', numero_valido)
