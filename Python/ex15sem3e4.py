quantosItens = int(input("Quantos itens serão adicionados? "))
lista = []

for itens in range (0, quantosItens):
    lista.append(input("Digite o produto: "))
    print("Sua lista de compras é:", lista)

print ("Essa é sua lista de compras final: ", lista)
