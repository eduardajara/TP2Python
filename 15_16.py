def entrada_aluno():
    """
    Solicita o nome e as notas do aluno e retorna o nome do aluno em str e suas notas em float.
    """
    nome = input('Insira o nome do aluno: ')
    if nome.lower() == "fim":
        return None, None, None
    
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    
    return nome, nota1, nota2

def calcular_aluno(nota1, nota2):
    """
    Calcula a média com as notas fornecidas e retorna elas em float sendo a média 
    aritmética das duas notas.
    """
    return (nota1 + nota2) / 2

def calcular_turma(medias):
    """
    Calcula a média de toda turma com base nas médias dos outros alunos e retorna a
    média geral da turma em float. Caso a lista esteja vazia retornará 0.

    Parâmetros -->  medias (list): lista com as médias de cada aluno.
    """
    if len(medias) == 0:
        return 0
    return sum(medias) / len(medias)

# Principal
medias_turma = []

while True:
    nome, nota1, nota2 = entrada_aluno()
    if nome is None:  # Termina a entrada com "fim"
        break
    
    media_aluno = calcular_aluno(nota1, nota2)
    medias_turma.append(media_aluno)
    
    # Mostra a média do aluno e seu status
    print(f"Média = {round(media_aluno, 1)}")
    if media_aluno >= 6:
        print("Aluno aprovado")
    else:
        print("Aluno de recuperação")

# Calcula e exibe a média da turma
media_geral = calcular_turma(medias_turma)
print(f"\nMédia da turma = {round(media_geral, 1)}")
