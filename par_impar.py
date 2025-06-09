import os as o

def par_impar(numero):
     if numero %2 == 0:
        print("O Número é par !!")
     else:
        print("O número é impar !!")

if __name__=='__main__':

    o.system('cls' if o.name == 'nt' else 'clear')
    while True:
     try:
       numero=int(input("Digite um número: "))
       par_impar(numero)
       break

     except ValueError:
        print('Por favor, digite apenas números inteiros válidos.')
        input('Pressione Enter para continuar...')



    print('Fim do Programa')
