import re as r
import os as o

def validador(cpf):
    padrao= r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    resultado= r.search(padrao,cpf)
    if resultado:
        print("O CPF é Válido")
    else:
        print("O CPF é inválido")

if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    cpf=input ("Digite o CPF: ")
    validador(cpf)
    print("Fim do Programa !!")
