def sua_vendas():
    valores = input("Digite os valores das vendas: ").split()
    total = sum(map(float, valores))
    print(f"O total de vendas foi: R$ {total:.2f}")

if __name__=="__main__":
   sua_vendas()