def lista():
   produtos = input("Digite os produtos separados por vírgula: ").split(",")
   precos = input("Digite os preços separados por vírgula: ").split(",")
   for produto, preco in zip(produtos, precos):
       print(f"{produto.strip()}: {preco.strip()}")


if __name__=='__main__':
    lista()