import os as o

def unir_lista():
    laura = set(input("Digite a lista da Laura (Itens separados por vírgula): ").split(","))
    ana = set(input("Digite a lista da Ana (Itens separados por vírgula): ").split(","))
    comuns = laura.intersection(ana)
    exclusivos_laura = laura.difference(ana)
    exclusivos_ana = ana.difference(laura)
    print(f"Itens em ambas as listas: {', '.join(comuns)}")
    print(f"Itens exclusivos de Laura: {', '.join(exclusivos_laura)}")
    print(f"Itens exclusivos de Ana: {', '.join(exclusivos_ana)}")


if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    unir_lista()
