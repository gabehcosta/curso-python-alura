import random


def jogar():

    print("**************************************")
    print("*  Seja Bem vindo ao jogo de Forca!  *")
    print("**************************************")

    palavras = []
    with open("projeto-padrao/palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice].upper()

    letras_certas = ["_" for letra in palavra_secreta]

    print(letras_certas)

    acertou = False
    enforcou = False
    
    tentativas = 5
    print("Você tem {} tentativas".format(tentativas))

    while(not acertou and not enforcou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                
                if(chute == letra):
                    letras_certas[index] = letra

                index += 1

        else:
            tentativas -= 1
            print("Você tem {} tentativas".format(tentativas))

        enforcou = tentativas == 0
        acertou = "_" not in letras_certas

        print(letras_certas)

        if(acertou):
            print("Parabéns, você ganhou!!! A palavra secreta era {}".format(palavra_secreta))
        elif(enforcou):
            print("Que pena, você perdeu!!! A palavra secreta era {}".format(palavra_secreta))

    print("\nFim de Jogo!")

if(__name__ == "__main__"):
    jogar()