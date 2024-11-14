def calc_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calc_fatorial(n - 1)
    
while True:
    numero = int(input('Insira um numero inteiro positivo (use 0 para encerrar o programa):'))
    
    if numero == 0:
        break

    if numero > 0:
        fatorial = calc_fatorial(numero)
        print(f"O fatorial de {numero} é: {fatorial}")
    else:
        print("Erro: insira um numero positivo")