import re as r
import os

def validador(nome, data):
    padrao = r'^(\d{2})/(\d{2})/(\d{4})$'
    resultado = r.search(padrao, data)

    if resultado:
        dia, mes, ano = resultado.groups()
        print(f"O nome é {nome}")
        print(f"Data de nascimento: {dia}/{mes}/{ano}")
    else:
        print("Data em formato inválido (esperado: dd/mm/aaaa)")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input('Digite o nome: ')
    data = input('Digite a data de nascimento (dd/mm/aaaa): ')
    validador(nome, data)  # Corrigido aqui também!
    print("Fim do programa !!")
