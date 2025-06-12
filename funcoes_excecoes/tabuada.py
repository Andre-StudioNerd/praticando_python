def tabuada():
    while True:

        try:
         numero_tabuada=int(input("Digite um número para a tabuada:"))
         for i in range(1,11):
            resultado=numero_tabuada * i
            print(f"{numero_tabuada} x {i} = {resultado}")
         break

        except ValueError:
          print('Por favor, digite apenas números inteiros válidos.')
          input('Pressione Enter para continuar...')
        continue

    print('Fim do Programa')

if __name__=="__main__":
  tabuada()