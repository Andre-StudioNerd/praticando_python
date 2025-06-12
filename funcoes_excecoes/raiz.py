import math as m
import os as o

def calculo():
    while True:
     o.system('cls' if o.name == 'nt' else 'clear')
     try:
      numero=int(input('Digite um número inteiro :'))
      print(f'A raiz quadrada de {numero} é {m.sqrt(numero):.2f}')
      print('Fim do Programa')
      break

     except ValueError:
        print('Por favor, digite apenas números inteiros válidos.')
        input('Pressione Enter para continuar...')

if __name__ == '__main__':
    calculo()