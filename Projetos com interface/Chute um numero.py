from random import randint

random = randint(1, 20)
chance = 10
chute = 0

while chance != random:
    chute = input("Advinhe um número de 1 a 20: ")
    if chute.isnumeric():
        chute = int(chute)
        chance = chance - 1
        if chute == random:
            print('')
            print('Uhruuuuu! Você acetou o número era {} e tinha {} tentativas'.format(random, chance))
            print(' ')
            break

        else:
            print('')
            if chute > random:
                print('Você errou!!! Dica: É um número menor.')
            else:
                print('')
        if chute < random:
            print('Você errou!!! Dica: É um número maior.')
            print('Voce ainda tem {} tentativas'.format(chance))
            print(" ")

        if chance == 0:
            print(' ')
            print('OH, não suas tentativa se esgotaram')
            print(' ')
            break

print("------- Fim de jogo ------")