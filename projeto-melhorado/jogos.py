import adivinhacao, forca

#######################################################################

#Função Principal
def executar():
    
    mensagem_boas_vindas()

    escolha = solicita_entrada()

    num_valido = False
    num_inteiro = False

    while(num_valido is False and num_inteiro is False):
        if(type(escolha) is int):
            
            if(escolha == 1 or escolha == 2 or escolha == 0):
                num_valido = True
                num_inteiro = True
                if(escolha == 1):
                    print("Você escolheu o jogo de Adivinhação!\n\n")
                    adivinhacao.executar()
                elif(escolha == 2):
                    print("Você escolheu o jogo de Forca!\n\n")
                    forca.executar()
                else:
                    print("Até a próxima, volte sempre!!\n\n")
                    break

            else:
                print("Numero não está nas opções")
                num_valido = False
                escolha = solicita_entrada()

        else:
            print("Entrada invalida")
            num_inteiro = False
            escolha = solicita_entrada()

#######################################################################

#Funções
def mensagem_boas_vindas():
    print("************************")
    print("*    Seja Bem-Vindo    *")
    print("************************")

def solicita_entrada():
    print("Escolha um jogo:")
    print("1 - Adivinhação / 2 - Forca / 0 - Sair")
    entrada = input("=> ")
    entrada = converte_str_para_int(entrada)
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