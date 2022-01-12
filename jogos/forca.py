def jogar():

    print("**************************************")
    print("*  Seja Bem vindo ao jogo de Forca!  *")
    print("**************************************")

    palavra_secreta = "banana"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):

        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Letra {} foi encontrada na posição {}".format(letra, index))
            
            index += 1

    print("\nFim de Jogo!")

if(__name__ == "__main__"):
    jogar()