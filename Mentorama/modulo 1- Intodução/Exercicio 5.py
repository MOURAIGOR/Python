s = 'Mentorama'
print("Em maiúsculo:", s.upper())
print ( "De trás para frente:",s [::-1])

for index, letra in enumerate(s):
    if letra in "aeiou":
        print("As vogais são: '%c' " % (letra))
