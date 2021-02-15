metros = int(input("Quantos metros vai ser pintado? "))
litros = metros/3 

preço = 80.0
capacidade = 18

latas = litros / capacidade
total = latas  * preço

print("Você usarar %d latas de tinta" %latas)
print("O preço total é de R$ %.2f" %total)
