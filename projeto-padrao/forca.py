def jogar():

    print("**************************************")
    print("*  Seja Bem vindo ao jogo de Forca!  *")
    print("**************************************")

    palavra_secreta = "banana".upper()
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
            print("Parabéns, você ganhou!!!")
        elif(enforcou):
            print("Que pena, você perdeu!!")

    print("\nFim de Jogo!")

if(__name__ == "__main__"):
    jogar()