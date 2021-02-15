# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8 %): R$
# d. - Sindicato (5 %): R$
# e. = Salário Liquido: R$

quanto_ganha = float(input("Qanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas trabalhada no mês? "))
salario_bruto = quanto_ganha * horas_trabalhadas
IR = (11/100 * salario_bruto)
print("Imposto de renda: R$: " ,IR)
INSS = (8/100 * salario_bruto)
print("INSS: R$: " ,INSS)
Sindicato = (5/100 * salario_bruto)
print("Sindicato: R$: " ,Sindicato)
desc = IR + INSS + Sindicato 
salario = salario_bruto - desc
print("O eu salario luiquido é R$: {}  e o total de desconto foi de R$: {}" .format(salario,desc))
