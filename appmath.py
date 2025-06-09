import os as o

def divisao(dividendo,divisor):
    return round(dividendo/divisor,2)

if __name__ =='__main__':
    while True:
        try:
            o.system('cls' if o.name == 'nt' else 'clear')
            numero1=int(input('Digite um número: '))
            numero2=int(input('Digite outro número: '))
            resultado=divisao(numero1,numero2)

        except ValueError:
            print('Digite um númeo inteiro válido')
            input('Pressione Enter para continuar...')
            continue
        except ZeroDivisionError:
            print('Não é possivel dividir por zero')
            input('Pressione Enter para continuar...')
            continue
        except:
            print('Erro desconhecido')
            input('Pressione Enter para continuar...')
            continue
        else:
            print(f'Resultado: {resultado}')
            break

        finally:
            print(f'\nFim do Programa')
