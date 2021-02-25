equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta="S"

while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(input("Valor: "))
    seriais.append(input("Numero Serial: "))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor...........: ", valores[indice])
    print("Serial..........: ",seriais[indice])
    print("Departamento....: ", departamentos[indice])


busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor...: ", valores[indice])
        print("Serial..: ", seriais[indice])


depreciacao=input("\Digite o equipamento que sera depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ",valores[indice])
        valores[indice] = valores[indice]
        print("Novo valor: ",valores[indice])

serial=int(input("\nDigite o serial do equipamento que sera excluido: "))
for indice in range(0,len(departamentos)):
    if seriais[indice]==serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor...........: ", valores[indice])
    print("Serial..........: ",seriais[indice])
    print("Departamento....: ", departamentos[indice])
