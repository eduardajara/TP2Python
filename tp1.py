def c_vogais():
    qnt_vogais = 0
    vogais = 'aeiouAEIOU'
    
    while True:
        caractere = input("Insira um caractere: ")
        
        if caractere == '.':
            break
        
        if caractere in vogais:
            qnt_vogais += 1
            
    return qnt_vogais

num_vogais = c_vogais()
print(f'O Número de vogais é: {num_vogais}')