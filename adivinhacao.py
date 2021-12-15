print("**************************************")
print("Seja Bem vindo ao jogo de Adivinhação!")
print("**************************************")

num_secreto = 13
chute = int(input("Digite o seu chute: "))

if(num_secreto == chute):
    print("Você Acertou!!!")
else:
    print("Você Errou!!!")