import os as o

def lista_convidados():
 convidados = set()
 while True:
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ")
    if nome.lower() == "sair":
     break
    convidados.add(nome)
 print(f"Convidados confirmados: {', '.join(convidados)}")

if __name__=='__main__':
   o.system('cls' if o.name == 'nt' else 'clear')
   lista_convidados()

