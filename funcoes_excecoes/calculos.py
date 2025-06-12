import math
import os as o

def logaritimo(valor):
    log=math.log10(valor)
    print(f'O logarítmo de {valor} é {log:.4}')

def fatorial(valor):
     fat=math.factorial(valor)
     print(f'O fatorial do {valor} é {fat}')

def raiz_cubica(valor):
     raiz=math.pow(valor,1/3)
     print (f'A raiz cúbica de {valor} é {raiz:.2f}')


if __name__ == '__main__':
    while True:
       try:
           o.system('cls' if o.name == 'nt' else 'clear')
           valor=int(input('Digite um número inteiro : '))
           logaritimo(valor)
           fatorial(valor)
           raiz_cubica(valor)
           break
       except ValueError:
               print('Por favor, digite apenas números inteiros válidos.')
               input('Pressione Enter para continuar...')
