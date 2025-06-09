def seunome():
    while True:
        try:
          nome=input('Digite seu nome ou x para finalizar: ')
          if nome =='x' or nome=='X':
           break
          else:
           print(f'Bem vindo: {nome}')
           break

        finally:
         print('FIM do Programa')


if __name__ == '__main__':
    seunome()
