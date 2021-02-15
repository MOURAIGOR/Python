n1 = float(input("Digite sua 1° nota: "))
n2 = float(input("Digite sua 2° nota: "))

nota = (n1 + n2 ) / 2

if nota >= 7 and nota < 10:
    print("Aprovado")

elif nota >= 10:
    print("Aprovado com distinção")

else:
    print("Reprovado")    
