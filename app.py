import os

restaurantes = ['Nono','Super']

def exibir_nome_do_programa():
    print('Sabor Express')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o app')

def cadastrar_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Cadastro de restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado')
    input('Digite uma tecla para voltar ao menu')

def listar_restaurantes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Listando restaurantes:')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    input('Digite uma tecla para voltar ao menu')

def ativar_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Função de ativar restaurante ainda não implementada.')
    input('Digite uma tecla para voltar ao menu')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                cadastrar_restaurante()
            elif opcao_escolhida == 2:
                listar_restaurantes()
            elif opcao_escolhida == 3:
                ativar_restaurante()
            elif opcao_escolhida == 4:
                finalizar_app()
                break
            else:
                print('Opção inválida.')
                input('Pressione Enter para continuar...')
        except ValueError:
            print('Por favor, digite um número válido.')
            input('Pressione Enter para continuar...')

if __name__ == '__main__':
    main()
