import os as o

def lista_produtos():
    dicionario_produtos = {}
    for i in range(3):
      nome = input("Digite o nome do produto: ")
      while True:
       try:
        quantidade = int(input("Digite a quantidade: "))
        break
       except ValueError:
        print('Por favor, digite apenas números inteiros válidos.')
        input('Pressione Enter para continuar...')

      dicionario_produtos[nome] = quantidade
    print(f"Dicionário de produtos: {dicionario_produtos}")

if __name__=='__main__':
   o.system('cls' if o.name == 'nt' else 'clear')
   print('Programa cadastro de produtos')
   lista_produtos()