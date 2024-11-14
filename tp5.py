def gerar_pa (prim_termo, razao, qnt_termos):
    termos = [prim_termo + razao * i for i in range(qnt_termos)]
    return termos

prim_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
qnt_termos = int(input('Insira a quantidade de termos para ser gerado: '))

pa = gerar_pa(prim_termo, razao, qnt_termos)
print(f'A progressão arim[etrica gerada é de: {pa}')