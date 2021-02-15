par = []
impar = []

for count in range( 1, 11):
    if count % 2 == 0:
        par.append(count)
           
    else:
        impar.append(count)
     
print ('A quantidade de numeros pares sao {} e impares {}.'.format(len(par), len(impar)))
print ('A soma de todos os valores par e {} e {} impares' .format(sum(par), sum(impar)))