def perguntar():
    resposta= input("O que deseja realizar? \n"+
            "<I> - Para Inserir um usuario \n"+
            "<P> - Para Pesquisar um usuario \n"+
            "<E> - Para Excluir um usuario \n"+
            "<L> - Para Listar um usuario: ").upper()
    return resposta

def inserir(dicionario): 
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
        input("Digite a ultima data de acesso: "),
        input("Digite a ultima estacao acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!= None:
        print("Nome.........: " + lista[0])
        print("Ultimo acesso....: " + lista[1])
        print("Ultima estacao...: " + lista[2])

def excluir(dicionario,chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave,valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ",valor)
