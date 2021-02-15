import random
dado = []

print("Bem vindo ao jogo de dados!")

while True:
    dado.clear()
    
    while True:
        resp = str(input("Gostaria de lançar os dados? (S/N):")).upper()[0]
        if resp in 'SN':
            break
        print ("Digite apenas S ou N")

    if resp == 'S':
        print('Oba, o seu resultado é: ',random.randint(1,6))

    if resp == 'N':
        print('Ok, deixa para uma proxima vez!')
