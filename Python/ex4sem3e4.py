grauA = float(input("Digite a nota do grau A: "))
grauB = float(input("Digite a nota do grau B: "))
notaFinal = grauA * 0.3 + grauB * 0.7

if notaFinal < 6:
    print("Você precisará fazer o grau C, pois sua nota final é: ", notaFinal)
elif notaFinal > 6:
    print("Você não vai precisar fazer o grau C, sua nota final é: ", notaFinal)
else:
    print("Alguma das notas tem um número inválido")