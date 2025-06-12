import os as o

def lista_participantes(participantes):
     print('Lista de Participantes: ')
     print(participantes)
     print()

def remove_participantes(participantes):
    nome_remover = input("Digite o nome do participante a ser removido: ")
    for workshop, nomes in participantes.items():
     nomes.discard(nome_remover)
    print()
    print("Lista atualizada de participantes:")
    for workshop, nomes in participantes.items():
      print(f"{workshop}: {nomes}")

if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    participantes = { "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
                 "Workshop 2": {"Fernanda", "Gustavo", "Helena"}}
    lista_participantes(participantes)
    remove_participantes(participantes)