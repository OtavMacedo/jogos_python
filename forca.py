import random


def jogar():
    print("****************************************")
    print("******_Bem vindo ao jogo da Forca_******")
    print("****************************************\n")

    arquivo = open("arquivo.txt", "r")
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()

    palavra_secreta = palavras[random.randrange(len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Restam {} tentativas".format(6 - erros))

        acertou = letras_acertadas.count("_") == 0
        enforcou = erros == 6
        print(letras_acertadas)

    if acertou:
        print("Parabéns, você ganhou!")
    elif enforcou:
        print("Você perdeu, tente novamente!")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
