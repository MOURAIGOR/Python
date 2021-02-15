Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randint

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