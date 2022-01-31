import random

#######################################################################

#Função principal
def executar():
    imprime_mensagem_bem_vindo()
    palavra_secreta = define_palavra_secreta()

    letras_certas = inicializa_letras_certas(palavra_secreta)

    ganhou = False
    enforcou = False

    erros = 0
    
    desenha_forca(erros)
    print(letras_certas)

    while(not ganhou and not enforcou):
        chute = solicita_chute()

        if(chute in palavra_secreta):
            desenha_forca(erros)
            marca_chute_correto(palavra_secreta, chute, letras_certas)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        ganhou = "_" not in letras_certas

        print(letras_certas)

        if(ganhou):
            imprime_mensagem_vencedora(palavra_secreta)

        elif(enforcou):
            imprime_mensagem_perdedora(palavra_secreta)

    print("\nFim de Jogo!")

#######################################################################

#Funções
def imprime_mensagem_bem_vindo():
    print("**************************************")
    print("*  Seja Bem vindo ao jogo de Forca!  *")
    print("**************************************")

def define_palavra_secreta():
    palavras = []
    with open("projeto-padrao/frutas.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice].upper()

    return palavra_secreta

def inicializa_letras_certas(palavra):
    return ["_" for letra in palavra]

def solicita_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_certas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_certas[index] = letra
        index += 1

def imprime_mensagem_vencedora(palavra_secreta):
    print("Parabéns, você ganhou!!! A palavra secreta era {}".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedora(palavra_secreta):
    print("Que pena, você perdeu!!! A palavra secreta era {}".format(palavra_secreta))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         \n")

#######################################################################

#Verificação de abertura do programa
if(__name__ == "__main__"):
    executar()