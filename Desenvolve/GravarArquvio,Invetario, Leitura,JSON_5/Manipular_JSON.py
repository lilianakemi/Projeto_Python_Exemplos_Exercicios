import json
inventario={}
opcao=int(input("Digite: "
                    "\n<1> para registrar ativo"
                    "\n<2> para exibir ativos armazenados: "))
while opcao>0 and opcao<3: 
    if opcao==1:
        resp="S"
        while resp=="S":
            inventario[input("DIgite o numero patrimonial: ")]=[
                input("Digite a data da ultima atualizacao: "), 
                input("Digite a descricao: "), 
                input("Digite o departamento: ")]
            resp=input("Digite <S> para continuar. ").upper()
        with open("inventario_json.json", "w") as arq_json: 
            json.dump(inventario, arq_json)
        print("Json gerado!!!")
    elif opcao==2: 
        with open("inventario_json.json", "r") as arq_json:
            resultado=json.load(arq_json)
            for chave, dado in resultado.items():
                print("Data..........: ", dado[0])
                print("Descricao.....: ", dado[1])
                print("Departamento..: ", dado[2])
    opcao = int(input("Digite: "
                "\n<1> para registrar ativo"
                "\n<2> para exibir ativos armazenados: "))
