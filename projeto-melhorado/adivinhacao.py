import random

#Função de execução do programa
def executar():

    #Título do jogo
    print("***************************")
    print("*   Jogo de Adivinhação   *")
    print("***************************")

    #Capturando e armazenando o nome do jogador
    nome_jogador = input("Qual é seu nome? -> ")
    nome_jogador = nome_jogador.capitalize()

    #Boas vindas e escolha da dificuldade
    print("\nOlá, {}. Seja bem-vindo!\nEscolha um nível para continuar:".format(nome_jogador))

    #Níveis
    facil = 1
    regular = 2
    dificil = 3

    #Verificando se a entrada do usuário é literal ou numérico e estabelecendo qtd de chances
    nivel = input("(1)Fácil\t(2)Regular\t(3)Difícil -> ")
    literal = True
    num_valido = False

    while(literal == True and num_valido == False):
            
        try:

            nivel = int(nivel)
            if(nivel == facil or nivel == regular or nivel == dificil):
                print("***************************")
                if(nivel == facil):
                    total_tentativas = 20
                    print("Nível escolhido: Fácil")
                elif(nivel == regular):
                    total_tentativas = 10
                    print("Nível escolhido: Regular")
                else:
                    total_tentativas = 5
                    print("Nível escolhido: Difícil")
                literal = False
                num_valido = True

            else:
                print("Digite um nível válido!!")
                nivel = input("(1)Fácil\t(2)Regular\t(3)Difícil -> ")
                
        except ValueError:
            print("Digite um nível válido!!")
            nivel = input("(1)Fácil\t(2)Regular\t(3)Difícil -> ")


    #Gerador do número secreto
    num_secreto = random.randrange(1, 101)

    print("Tente encontrar o número secreto!! (De 1 à 100)")

    #Loop de tentativas
    for tentativa_atual in range(1, total_tentativas + 1):
    
        print("\nTentativa {} de {} restantes".format(tentativa_atual, total_tentativas))
        chute = input("Chute: ")

        try:
            chute = int(chute)
            if(chute > num_secreto):
                print("O número secreto é MENOR do que {}".format(chute))

            elif(chute < num_secreto):
                print("O número secreto é MAIOR do que {}".format(chute))
            
            else:
                print("Parabéns, {}! Você ganhou! O número secreto era: {}".format(nome_jogador, num_secreto))
                print("Fim de Jogo...\n\n")
                break
        
        except ValueError:
            print("Digite um número por favor!")

        if(tentativa_atual == total_tentativas):
            print("\nVocê Perdeu! O número secreto era {}".format(num_secreto))
            print("Fim de Jogo...\n\n")

#Teste para execução do programa
if(__name__ == "__main__"):
    executar()