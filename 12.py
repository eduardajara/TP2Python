def estatisticas(lista):
    menor = lista[0]
    maior = lista[0]
    soma = 0
    
    for numero in lista:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero
    
    media = soma / len(lista)
    
    print(f'Menor: {menor}')
    print(f'Maior: {maior}')
    print(f'Soma: {soma}')
    print(f'Média: {media}')

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

estatisticas(lista)
