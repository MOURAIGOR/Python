# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8 %): R$
# d. - Sindicato (5 %): R$
# e. = Salário Liquido: R$


quanto_ganha = float(input('Quanto voce ganha por hora? '))
horas_trabalhadas = int(input("Quantas horas trabalhadas? "))

salario_bruto = quanto_ganha * horas_trabalhadas
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
Sindicato = salario_bruto * 0.05

print("+ salario bruto R$ %.2f" %salario_bruto)
print("- IR: R$ %.2f" %IR) 
print("- INSS: R$ %.2f" %INSS)
print("- Sindicato: R$ %.2f" %Sindicato)
print("Salario liquido: R$ %.2f" %(salario_bruto - IR - INSS - Sindicato ))
