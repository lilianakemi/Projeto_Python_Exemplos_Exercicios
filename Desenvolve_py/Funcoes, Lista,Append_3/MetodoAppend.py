inventario=[]
resposta="S"
while resposta=="S":
    inventario.append(input("Equipamento: "))
    inventario.append(input("Valor: "))
    inventario.append(input("Numero Serial: "))
    inventario.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)


