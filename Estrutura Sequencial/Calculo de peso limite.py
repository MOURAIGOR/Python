peso_limite = 50
peso_peixe = float(input("Qual é o peso do peixe? "))

if peso_peixe > peso_limite:
    excesso = peso_peixe - peso_limite
    multa = excesso * 4.00    
    print("Peso do peixe está acima do permetido e terar um multa de: R$ {}".format(multa))

else:
    print("o peixe esta no peso permitido")
