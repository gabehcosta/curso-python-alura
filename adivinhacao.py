print("**************************************")
print("Seja Bem vindo ao jogo de Adivinhação!")
print("**************************************")

num_secreto = 13

chute = int(input("Digite o seu chute: "))
print("Você digitou o número:", chute)

acertou = (chute == num_secreto)
maior   = (chute > num_secreto)
menor   = (chute < num_secreto)

if(acertou):
    print("Parabéns, você Acertou!!!")
else:
    if(maior):
        print("Você Errou! O chute foi MAIOR que o número secreto")
    elif(menor):
        print("Você Errou! O chute foi MENOR que o número secreto")