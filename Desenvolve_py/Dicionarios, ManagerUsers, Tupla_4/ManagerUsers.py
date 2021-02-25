from Funcoes.Funcoes_Dicionarios import*
import time

usuarios={}
opcao=input("O que deseja realizar? \n"+
            "<I> - Para Inserir um usuario \n"+
            "<P> - Para Pesquisar um usuario \n"+
            "<E> - Para Excluir um usuario \n"+
            "<L> - Para Listar um usuario: ").upper()
while opcao == "I" or opcao=="P" or opcao =="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a ultima data de acesso: ").upper()
        estacao=input("Digite a ultima estacao acessada: ").upper()
        usuarios[chave]=[nome,data,estacao]

# Poderia ser enxuto dessa forma:

#         chave=input("Digite o login: ").upper()
#         usuarios[chave]=[input("Digite o nome: ").upper(),
#                         input("Digite a ultima data de acesso: "), 
#                         input("Digite a ultima estacao acessada: ").upper()


# Ou mais resumido ainda ( tirando a variavel "chave"):

# usuarios[input("Digite o login: ").upper()=[input("Digite o nome: ").upper(), 
# input("Digite a ultima data de acesso: "), 
# input("Digite a ultima estacao acessada: ").upper()]


    opcao=input( "O que deseja realizar? \n" + 
                "<I> - Para Inserir um usuario \n"+
                "<P> - Para Pesquisar um usuario \n"+
                "<E> - Para Excluir um usuario \n"+
                "<L> - Para Listar um usuario: ").upper()


