a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b**2) - (4 * a * c)

if delta > 0:
    x1 = ((-b) + (delta ** 0.5)) / (2 * a)
    x2 = ((-b) - (delta ** 0.5)) / (2 * a)
    print("O valor é X1: {} e X2: {}".format(x1, x2))
elif delta == 0:
    x = (-b) / 2 * a
    print("Ha uma resolução: ", x)
else:
    print('Nao há possibilidade para raízes negativas')