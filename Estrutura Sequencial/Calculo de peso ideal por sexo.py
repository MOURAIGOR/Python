#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

Sexo = input("Qual é o seu sexo? (Informe 1 para homem ou 2 para mulher): ")
Peso = float(input("Digite seu peso:"))
Altura= float(input("Digite sua altura:"))

if Sexo == 1: 
   peso_ideal_h = (72.7 * Altura) - 58
   print ('seu peso ideal é:',peso_ideal_h,'kg') 

elif Sexo == 2:
   peso_ideal_m = (62.1 * Altura) - 44.7 
   print ('Seu pedo ideal é:',peso_ideal_m,'Kg')
   
