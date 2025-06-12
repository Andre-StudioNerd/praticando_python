import os as o

def vendas(produtos):
  estoque=produtos

  while estoque>0:
     print(f'Venda realizada ! Esoque restante: {estoque-1}')
     estoque-=1
  print('Estoque esgotado !!')

if __name__=='__main__':
   while True:
    try:
        o.system('cls' if o.name == 'nt' else 'clear')
        produtos=int(input('Digite o número de prudutos: '))
        vendas(produtos)
        break
    except ValueError:
        print('Por favor, digite apenas números inteiros válidos.')
        input('Pressione Enter para continuar...')
