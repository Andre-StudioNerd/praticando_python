import os as o

def etaria(idade):
    if 0<idade<=12:
        print('Criança')
    elif 12<idade<=18:
        print('Adolescente')
    elif idade > 18:
        print('Adulto')
    else:
        print('Valor inválido')

if __name__=='__main__':
 while True:
    try:
     o.system('cls' if o.name == 'nt' else 'clear')
     idade=int(input("Digite uma idade em anos: "))
     etaria(idade)
     break

    except ValueError:
         print('Por favor, digite apenas números inteiros válidos.')
         input('Pressione Enter para continuar...')

print('Fim do Programa')
