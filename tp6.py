def ver_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def num_primos_intervalo(inf, sup):
    primos = []
    for num in range(inf, sup + 1):
        if ver_primo(num):
            primos.append(num)
    return primos

inf = int(input("Insira o limite inferior do intervalo: "))
sup = int(input("Insira o limite superior do intervalo: "))

primos = num_primos_intervalo(inf, sup)

print(f"Os números primos no intervalo de {inf} a {sup}: {primos}")
print(f"A quantidade de números primos encontrados: {len(primos)}")
