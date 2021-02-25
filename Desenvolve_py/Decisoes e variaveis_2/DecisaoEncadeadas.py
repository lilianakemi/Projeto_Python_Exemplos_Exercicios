nome=input("Digite o nome: ")
idade=int(input("Digite a idade"))
doenca_infect= input("Suspeita de doenca infecto-contagiosa?").upper()


# Primeiro caso a ser resolvido - doenca infecto contagiosa 

if doenca_infect=="SIM":
    print("Encaminhe para a sala AMARELA")
elif doenca_infect=="NAO":
    print("Encaminhe para a sala BRANCA")
else:
    print("Responda a suspeita de doenca infectocontagiosa com SIM ou NAO")

if idade>=65: 
    print("Paciente com prioridade") 
 
else:
    genero= input("Digite o genero do paciente").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está gravida?").upper()
        if gravidez=="SIM":
            print("Paciente com prioridade")
        else:
            print("Paciente sem prioridade")
    else:
        print("Paciente sem prioridade")




