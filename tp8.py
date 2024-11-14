lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]

resultado = []

for i in range(len(lista1)):
    resultado.append(lista1[i] + lista2[i])

print("A soma das listas seria é:")
print(resultado)
