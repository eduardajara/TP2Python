import random

num_inicial = random.randint(1, 100)
num_final = random.randint(1, 100)

soma = sum(range(num_inicial, num_final +1))

media = soma/(num_final - num_inicial +1)

print(f'A soma dos numeros de {num_inicial} a {num_final} é de {soma}')
print(f'A média dos numeros de {num_inicial} a {num_final} é de {media}')