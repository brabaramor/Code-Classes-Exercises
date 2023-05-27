def tipoDePele ():
  if caracteristicaPele == 1:
    print("Sua pele é oleosa")
  if caracteristicaPele == 2:
    print("Sua pele é seca")
  if caracteristicaPele() == caracteristicaPele != 1 and caracteristicaPele () == caracteristicaPele != 2:
    print("Número inválido. digite 1 pra cravos e espinhas e 2 para ressecamento")

nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
print("Olá",nome, "você tem ", idade, "anos. Queremos saber um pouco mais sobre sua pele, conta aqui:")
caracteristicaPele = input("Entre cravos e espinhas ou ressecamento, digite 1 pra cravos e espinhas e 2 para ressecamento: ")
tipoDePele()
