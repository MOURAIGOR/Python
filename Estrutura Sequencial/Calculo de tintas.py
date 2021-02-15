medida = float(input("Digite os metros quadrados: "))
litros = medida / 6
latas= litros // 18 + 1 
galões = litros // 3.6 + 1
preço_latas = latas * 80
preço_galões = galões * 25
combinação = (litros // 18 ) * 80  + ((litros % 18 ) // 3.6 + 1 ) * 25

print("O preço só com as latas é: R$ " ,preço_latas)
print("O preço so com os galões é: R$ ",preço_galões)
print("P preço com a combinação é: R$" ,combinação)
