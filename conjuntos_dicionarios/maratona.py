import os as o

def listar_participantes(participantes):
    print(f"Nomes dos participantes: {', '.join(participantes.keys())}")
    print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}")
    print("Participantes e suas idades:")
    for nome, idade in participantes.items():
        print(f"- {nome}: {idade} anos")

if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    participantes = {"Mariana": 25,"Carlos": 32,"Beatriz": 28,"Rafael": 35}
    listar_participantes(participantes)
