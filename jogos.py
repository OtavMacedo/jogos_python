import forca
import adivinhacao


print("****************************************")
print("**********_Escolha o seu jogo_**********")
print("****************************************\n")
print("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha um jogo: "))
if jogo == 1:
    forca.jogar()
elif jogo == 2:
    adivinhacao.jogar()
