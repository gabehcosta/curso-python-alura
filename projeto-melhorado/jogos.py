#Importando os arquivos dos jogos
import adivinhacao


#Função de execução do programa
def executar():

    #Título da tela de escolha
    print("***************************")
    print("*    Seja Bem-Vindo!!!    *")
    print("***************************")

    #Entrada e escolha do jogo pelo usuário
    print("\nEscolha um jogo para continuar")
    jogo_escolhido = input("(1)Adivinhação   (2)Forca   -> ")

    #Definição do ID dos jogos
    jogo_adivinhacao = 1
    jogo_forca = 2
    
    
#Teste para execução do programa
if(__name__ == "__main__"):
    executar()