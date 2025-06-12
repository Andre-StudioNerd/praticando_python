import os as o

def exibi_pessoa():
 o.system('cls' if o.name == 'nt' else 'clear')
 print('Programa Pesssoa')
 pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}
 print(pessoa)

# Atualização de Idade
 pessoa['idade'] = 31

# Adicionando Profissão
 pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
 del pessoa['cidade']

 print(pessoa)
 print()


def quadrado():

 print('Exibi os quadardos de 1 - 5')
 numeros_quadrados = {x: x**2 for x in range(1, 6)}
 print(numeros_quadrados)
 print()

def chave():
 print("Acha a chave")
 pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
 if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
 else:
    print("A chave 'nome' não existe no dicionário.")
print()

def contagem():
 print('Contagem de palavras')
 frase = "Python se tornou uma das linguagens"
 contagem_palavras = {}
 palavras = frase.split()
 for palavra in palavras:
     contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
     print(contagem_palavras)
     print()


if __name__=='__main__':
 exibi_pessoa()
 quadrado()
 chave()
 contagem()