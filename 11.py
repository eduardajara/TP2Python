def buscar(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
    return -1

lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]

numero = int(input('Insira o numero que deseja buscar: '))
posicao = buscar(lista, numero)

if posicao != -1:
    print(f'O numero {numero} foi encontrado na posição {posicao}')
else:
    print(f'O numero {numero} não foi encontrado')
