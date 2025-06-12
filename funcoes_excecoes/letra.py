def sua_palavra():
    letras=[]
    for letra in palavra:
        letras.append(letra)
    print(f'As letras separadas são: {letras}')

def contar_palavras():
    letras = [letra for letra in palavra if letra.isalpha()]
    print(f'As Quantidades de caracteres são: {len(letras)}')

if __name__ == '__main__':
    global palavra
    palavra =input('Digite a sua palavra: ')
    sua_palavra()
    contar_palavras()