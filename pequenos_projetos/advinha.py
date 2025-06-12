import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 20)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-20): "))

            if not 1 <= palpite <= 20:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 20.")

            tentativas += 1

            if palpite < numero_secreto:
                print("Baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break

        except ValueError as e:
            print(f"Entrada inválida: {e}")

if __name__=='__main__':
    adivinhar_numero()