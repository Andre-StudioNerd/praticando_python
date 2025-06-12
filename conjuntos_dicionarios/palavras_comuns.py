import os as o

def palavras_comuns():
    print('Programa Palvras Comuns')
    texto1 = set(input("Digite o Texto 1: ").lower().split())
    texto2 = set(input("Digite o Texto 2: ").lower().split())
    comuns = texto1.intersection(texto2)
    print(f"Palavras em comum: {comuns}")


if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    palavras_comuns()