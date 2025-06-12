import os as o

def exibi_estoque(estoque):
    print('Estoque Atual:')
    print(estoque)

def atualiza_produto(estoque):
    produto = input("Digite o nome do produto a ser atualizado: ")
    while True:
     try:
       nova_quantidade = int(input("Digite a nova quantidade: "))
       break

     except ValueError:
       print('Por favor, digite apenas números inteiros válidos.')
       input('Pressione Enter para continuar...')

    if produto in estoque:
       estoque[produto] = nova_quantidade
       print("Quantidade atualizada com sucesso!")
       print(estoque)
    else:
       print("Produto não encontrado no estoque.")

if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    estoque = {"Caderno universitário": 50,"Caneta azul": 120,"Borracha branca": 30}
    exibi_estoque(estoque)
    atualiza_produto(estoque)