def preencherInventario(lista):
    resp="S"
    while resp=="S":
        equipamento=[input("Equipamento: "),
            float(input("Valor: ")), 
            int(input("Numero Serial: ")), 
            input("Departamento: ")]
        lista.append(equipamento)
        resp=input("Digite \"s\" para continuar: ").upper()

def exibirInventario(lista): 
    for elemento in lista: 
        print("Nome......", elemento[0])
        print("Valor......", elemento[1])
        print("Serial......", elemento[2])
        print("Departamento......", elemento[3])
    
def localizarPorNome(lista):
    busca=input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista: 
        if busca==elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1]=elemento[1]* 0.9
            print("Novo valor: ", elemento[1])


def depreciarPorNome(lista):
    depreciar=input("Digite o nome do equipamento depreciado: ")
    for elemento in lista:
        if depreciar==elemento[0]:
            print("Valor antigo: ",elemento[1])
            elemento[1]=elemento[1]*0.7
            print("O novo valor eh: ", elemento[1])

def excluirPorSerial(lista):
    serial=int(input("Digite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2]==serial:
            lista.remove(elemento)
    return "Itens excluidos."


def resumirValores(lista):
    valores=[]
    for elemento in lista: 
        valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print( "O equipamento mais barato custa ", min(valores))
        print( "O total de equipamentos e de : ", sum(valores))

