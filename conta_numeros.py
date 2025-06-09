import os as o

def contador(numero):
  inicial=0
  while inicial < numero:
    inicial+=1
    print(f'Processando dados...{inicial}')


if __name__=='__main__':
 while True:
    try:
     o.system('cls' if o.name == 'nt' else 'clear')
     numero=int(input("Digite um número: "))
     contador(numero)
     break
    except ValueError:
       print('Por favor, digite apenas números inteiros válidos.')
       input('Pressione Enter para continuar...')
print('Fim do Programa !!')