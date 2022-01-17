


#Função de execução do programa
def executar():

    #Título do jogo
    print("***************************")
    print("*      Jogo da Forca      *")
    print("***************************")

    nome_usuario = input("Qual é o seu nome? -> ")
    nome_usuario = nome_usuario.capitalize()

    print("Olá, {}! Seja bem-vindo!!".format(nome_usuario))

    #Palavra secreta e lista de caracteres
    palavra_secreta = "banana".upper()
    

#Teste para execução do programa
if(__name__ == "__main__"):
    executar()