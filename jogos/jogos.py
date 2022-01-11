import adivinhacao
import forca

def executar():

    print("**************************************")
    print("           Seja Bem vindo!            ")
    print("**************************************")

    print("Escolha um jogo:")
    print("(1) Adivinhação  (2) Forca")

    jogo_escolhido = int(input("Jogo escolhido: "))
    jogo_adivinhacao = 1
    jogo_forca = 2

    if(jogo_escolhido == jogo_adivinhacao):
        adivinhacao.jogar()
    elif(jogo_escolhido == jogo_forca):
        forca.jogar()
    else:
        print("Insira uma opção válida!!")

if(__name__ == "__main__"):
    executar()