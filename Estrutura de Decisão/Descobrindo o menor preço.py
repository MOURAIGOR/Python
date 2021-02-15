n2 = input("Digite o 2° valor: ")
n3 = input("Digite o 3° valor: ")

def menor_valor ():
    if n1 < n2 and n3:
        print(n1,"é o mais barato.")

    elif  n2 < n1 and n3:
        print(n2,"é o mais barato.")    

    elif n3 < n1 and n2:
        print (n3,"é o mais barato.")    

# Se os valores for iguais 

    elif n1 == n2 and n3 :
        print (n1,"é o mais barato.")

    elif n2 == n1 and n3:
        print (n2,"é o mais barato")

    elif n3 == n1 and n2:
        print(n3,"é o mais bataro")    

menor_valor ()        
