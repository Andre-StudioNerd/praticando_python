import re as r
import os as o

def validador(email):
    padrao_email= r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    resultado=r.search(padrao_email,email)
    if resultado:
        print(f"Email válido: {resultado.group()}")

    else:
        print("Email inválido")


if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    email=input('Digite seu email :')
    validador(email)
    print("Fim do Programa !!")
