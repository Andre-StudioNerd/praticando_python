def avaliar():
    while True:
        try:
            primeiro_valor = int(input('Digite um Valor: '))
            segundo_valor = int(input('Digite outro Valor: '))

            if primeiro_valor > segundo_valor:
                print(f'Primeiro Valor = {primeiro_valor} é maior que o segundo valor = {segundo_valor}')
            elif primeiro_valor < segundo_valor:
                print(f'Primeiro Valor = {primeiro_valor} é menor que o segundo valor = {segundo_valor}')
            else:
                print('Os valores são iguais!')

            break  # Sai do loop se tudo ocorreu bem
        except ValueError:
            print('Por favor, digite apenas números inteiros válidos.')

if __name__ == '__main__':
    avaliar()
