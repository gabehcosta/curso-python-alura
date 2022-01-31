import random

#######################################################################

#Função principal
def executar():
    
    titulo_jogo()

    print("Seja bem-vindo(a), escolha um nível para continuar:")
    nivel_escolhido = escolhe_nivel()
    tentativas = define_tentativas(nivel_escolhido)

    print("Vamos começar, tente advinhar o numero secreto entre 1 e 100")

    venceu = False
    game_over = False

    num_secreto = random.randrange(1, 101)

    while(venceu is False and game_over is False):
        print("\nTentativas restantes: {}".format(tentativas))

        chute = solicita_entrada()
        if(chute == num_secreto):
            print("Parabéns, você acertou!!!")
            print("O número secreto era {}".format(num_secreto))
            venceu = True
        elif(chute > num_secreto):
            print("É menor.")
        else:
            print("É maior.")

        tentativas -= 1

        if(tentativas == 0):
            print("Você perdeu! Suas tentativas acabaram.")
            print("O número secreto era {}".format(num_secreto))
            game_over = True

    print("Fim do jogo!")

#######################################################################

#FUNÇÕES
def titulo_jogo():
    print("*************************")
    print("*  JOGO DA ADIVINHAÇÃO  *")
    print("*************************")

def escolhe_nivel():
    print("1 - Fácil\n2 - Médio\n3 - Difícil")
    entrada = input("=> ")
    entrada = converte_str_para_int(entrada)
    if(type(entrada) is int):
        if(entrada == 1):
            print("\nVocê escolheu o nível: FÁCIL")
            
        elif(entrada == 2):
            print("\nVocê escolheu o nível: MÉDIO")
            
        elif(entrada == 3):
            print("\nVocê escolheu o nível: DIFÍCIL")
            
        else:
            print("Opção inválida! Tenta novamente.")
            entrada = escolhe_nivel()
            
    else:
        print("Entrada inválida! Tente novamente.")
        entrada = escolhe_nivel()
        
    return entrada
        
def define_tentativas(nivel_escolhido):
    if(nivel_escolhido == 1):
        tentativas = 20
    elif(nivel_escolhido == 2):
        tentativas = 10
    else:
        tentativas = 5
    return tentativas

def solicita_entrada():
    entrada = input("=> ")
    entrada = converte_str_para_int(entrada)
    if(type(entrada) is int):
        return entrada
    else:
        print("Entrada inválida, digite um número inteiro!")
        entrada = solicita_entrada()
        return entrada

def converte_str_para_int(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        pass

#######################################################################

#Verificação de abertura do programa
if(__name__ == "__main__"):
    executar()