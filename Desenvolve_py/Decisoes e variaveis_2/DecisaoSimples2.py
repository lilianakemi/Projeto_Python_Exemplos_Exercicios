nome=input("Digite o nome: ")
idade=int(input("Digite a idade"))
doenca_infect= input("Suspeita de doenca infecto-contagiosa?").upper()

if idade>=65: 
    print("O paciente "+ nome + "tem atendimento prioritario!")

elif doenca_infect =="SIM": 
    print("O paciente " + nome + " precisa ir para uma sala reservada")

else:
    print("O paciente "+ nome + " nao tem atendimento prioritario!")



