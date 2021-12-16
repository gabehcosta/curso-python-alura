import random

print("**************************************")
print("Seja Bem vindo ao jogo de Adivinhação!")
print("**************************************")

num_secreto = random.randrange(1,101)
total_tentativas = 0
pontos = 1000

while(total_tentativas == 0):
    print("Escolha um nível de dificuldade:")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = input("Nível escolhido: ")
    facil   = (nivel == 1)
    medio   = (nivel == 2)
    dificil = (nivel == 3)

    if(facil):
        total_tentativas = 20
    elif(medio):
        total_tentativas = 10
    elif(dificil):
        total_tentativas = 5
    else:
        print("Escolha um nível válido!")

for tentativa_atual in range(1, total_tentativas + 1):

    print("Tentativa {} de {}".format(tentativa_atual,total_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou o número", chute)

    numero_invalido = (chute < 1 or chute > 100)

    if(numero_invalido):
        print("Você deve inserir um número entre 1 e 100!!!\n")
        continue

    acertou = (chute == num_secreto)
    maior   = (chute > num_secreto)
    menor   = (chute < num_secreto)

    if(acertou):
        print("Parabéns, você acertou!!!\n")
        break
    else:
        if(maior):
            print("Você Errou! O chute foi MAIOR que o número secreto\n")
        elif(menor):
            print("Você Errou! O chute foi MENOR que o número secreto\n")
        tentativa_atual += 1

print("Fim do Jogo!")