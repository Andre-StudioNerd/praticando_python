def filtrando():

    numeros = input("Digite os números separados por espaço: ").split()
    pares = filter(lambda x: int(x) % 2 == 0, numeros)
    print("Números pares:", " ".join(pares))

if __name__=="__main__":
    filtrando()