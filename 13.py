def eh_par(numero):
    return numero % 2 == 0

def separar(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if eh_par(numero):
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

pares, impares = separar(lista)

print('numeros pares:', pares)
print('numeros ímpares:', impares)
