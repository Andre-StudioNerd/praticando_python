import os

def calcula():
    notas = 2
    notas_aluno = []

    while notas > 0:
        try:
            nota = int(input("Digite a Nota:"))
            notas -= 1
            notas_aluno.append(nota)
        except ValueError:
            print('Por favor, digite apenas números inteiros válidos.')
            input('Pressione Enter para continuar...')
    return notas_aluno # <- retorna a lista

def exibi_notas(nome,notas_alunos):
    notas_alunos.sort(reverse=True)
    print(f"O nome do aluno é: {nome}")
    print("Notas do aluno:", notas_alunos)

def media(notas_alunos):

     if notas_alunos:  # verifica se a lista não está vazia
        nota_final = sum(notas_alunos) / len(notas_alunos)
        print(f"Média das notas: {nota_final:.2f}")
        return nota_final # <--Retorna media_final
     else:
        print("Nenhuma nota disponível para calcular a média.")

def analise(nota_final):

    if nota_final is None:
        print("Não é possível analisar sem média.")
    elif nota_final >= 7:
        print("Aprovado")
    elif nota_final >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do aluno: ")
    notas_alunos = calcula()  # <- captura a lista retornada
    exibi_notas(nome,notas_alunos)
    nota_final = media(notas_alunos)  # captura a média retornada
    analise(nota_final)
