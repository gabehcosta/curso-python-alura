print("**************************************")
print("Seja Bem vindo ao jogo de Adivinhação!")
print("**************************************")

num_secreto = 13
tentativa_atual = 1
total_tentativas = 3

while(tentativa_atual <= total_tentativas):

    print("Tentativa {} de {}".format(tentativa_atual,total_tentativas))

    chute = int(input("Digite o seu chute: "))
    print("Você digitou o número", chute)

    acertou = (chute == num_secreto)
    maior   = (chute > num_secreto)
    menor   = (chute < num_secreto)

    if(acertou):
        print("Parabéns, você acertou!!!\n")
        tentativa_atual = 4
    else:
        if(maior):
            print("Você Errou! O chute foi MAIOR que o número secreto\n")
        elif(menor):
            print("Você Errou! O chute foi MENOR que o número secreto\n")
        tentativa_atual += 1

print("Fim do Jogo!")