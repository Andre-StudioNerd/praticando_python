import os as o

def seu_planeta(planeta):
    if planeta.capitalize() in planeta_anao:
        print(f'{planeta} é um planeta anão!')
    else:
        print(f'{planeta} não é um planeta anão.')

def lista_planetas(planeta_anao):
    astros_set=set(planeta_anao)
    print(f'Lista de planesta anões = {astros_set}')

if __name__ == '__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    planeta_anao ={'Plutão', 'Ares','Iris'}
    planeta=input('Digite o nome do Planeta :')
    seu_planeta(planeta)
    lista_planetas(planeta_anao)
