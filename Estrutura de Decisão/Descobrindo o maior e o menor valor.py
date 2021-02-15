n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceito valor: "))

def maior_valor () :
    if n1 > n2 and n1 > n3:
        print(n1,"é o maior valor.")

    elif n2 > n1 and n2 > n3:
        print(n2,"é o maior valor.")

    elif n3 > n1 and n3 > n2:
        print(n3,"é o maior valor.")

# se os números for iguais

    elif n1 == n2 and n1 and n2 > n3:
        print(n1, "é o maior número.")


    elif n1 == n3 and n1 and n3 > n2:
        print(n1, "é maior número.")

    elif n2 == n3 and n2 and n3 > n1:
        print(n2, "é maior número.")


def menor_valor () :
    if n1 < n2 and n3:
        print(n1,"é o menor valor")

    elif n2 < n1 and n3:
        print (n2,"é o menor valor")

    elif n3 < n1 and n3:
        print(n3,"é o menor valor")

# se for numeros iguais

    elif n1 == n2 and n1 and n2 < n3:
        print(n1, "é o menor número.")

    elif n1 == n3 and n1 and n3 < n2:
        print(n1, "é menor número.")

    elif n2 == n3 and n2 and n3 < n1:
        print(n2, "é menor número.")

maior_valor ()
menor_valor ()
