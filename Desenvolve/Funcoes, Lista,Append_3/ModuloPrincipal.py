from IdentificacaoDeFuncoes import*

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Pequisando")
localizarPorNome(minhaLista)

print("Alterando")
depreciarPorNome(minhaLista)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
