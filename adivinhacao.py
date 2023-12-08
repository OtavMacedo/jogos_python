import random


def jogar():
    print("****************************************")
    print("***_Bem_vindo_ao_jogo_de_adivinhação_***")
    print("****************************************\n")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Escolha o nível de dificuldade")
    print("1-Fácil 2-Médio 3-Difícil")

    nivel = int(input("Escolha: "))
    if nivel == 1:
        total_de_tentativas = 12
    elif nivel == 2:
        total_de_tentativas = 8
    else:
        total_de_tentativas = 5

    print("Digite um número entre 1 e 100\n")

    for tentativa in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute = int(input("Digite um número: "))

        if chute < 1 or chute > 100:
            print("\n Você deve digitar um número entre 1 e 100")
            continue

        if chute == numero_secreto:
            print("\nParabéns, você acertou!")
            print("Sua pontuação foi: {}".format(pontos))
            break
        else:
            if chute > numero_secreto:
                print("\nVocê errou! O número secreto é menor que {}!".format(chute))
            elif chute < numero_secreto:
                print("\nVocê errou! O número secreto é maior que {}!".format(chute))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if tentativa == total_de_tentativas:
            print("\nSuas tentativas acabaram")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
