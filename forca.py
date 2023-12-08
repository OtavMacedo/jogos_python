import random


def jogar():
    mensagem_de_abertura()
    palavra_secreta = carregando_palavra_secreta()

    letras_acertadas = espacos_vazios_palavra(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Você errou! Restam {} tentativas".format(7 - erros))

        acertou = letras_acertadas.count("_") == 0
        enforcou = erros == 7
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    elif enforcou:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra secreta era {}".format(palavra_secreta))


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def espacos_vazios_palavra(palavra):
    return ["_" for letra in palavra]


def mensagem_de_abertura():
    print("****************************************")
    print("******_Bem vindo ao jogo da Forca_******")
    print("****************************************\n")


def carregando_palavra_secreta():
    arquivo = open("arquivo.txt", "r")
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()

    palavra_secreta = palavras[random.randrange(len(palavras))].upper()
    return palavra_secreta


if __name__ == "__main__":
    jogar()
