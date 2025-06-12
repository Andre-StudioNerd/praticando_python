import os

restaurantes = [{'nome':'Naruto Sushi', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
                ]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('Sabor Express')

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o app')

def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Cadastro de restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado')
    input('Digite uma tecla para voltar ao menu ')

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista

    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Listando restaurantes:')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
       nome_restaurante = restaurante['nome']
       categoria = restaurante['categoria']
       ativo = restaurante['ativo']
       ativo = 'ativado' if restaurante['ativo'] else 'desativado'
       print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    input('Digite uma tecla para voltar ao menu ')

def ativar_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante

    Outputs:
    - Exibe mensagem indicando o sucesso da operação'''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
     print('O restaurante não foi encontrado.')
    input('Digite uma tecla para voltar ao menu ')

def main():
    ''' Solicita e executa a opção escolhida pelo usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
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
