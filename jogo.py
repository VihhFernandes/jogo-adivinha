import random

def jogo_advinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação")
    print("Estou pensando em um número de 1 a 100.")

    while True:
        try:
            palpite = int(input("digite o seu palpite:"))
            tentativas += 1

            if palpite < numero_secreto:
                print("muito baixo!")
            elif palpite > numero_secreto:
                print("muito alto!")
            else:
                print(f"parabéns! você adivinhou o número em {tentativas} tentativas.")
                break
        except ValueError:
            print("por favor digite um número válido.")

if __name__ == "__main__":
   jogo_advinhacao()