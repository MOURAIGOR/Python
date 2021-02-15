n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))

if n1 > n2 and  n1 > n3: 
    print(n1,"é o maior número!!")

elif n2 > n1 and n2 > n3:
    print(n2,"e o maior número!!")

elif n3 > n2 and n3 > n1:
    print(n3,"é o maior número!!")  

# se os números for iguais 

elif n1 == n2 and n1 and n2 > n3:
    print(n1,"é o maior número.")

elif n1 == n3 and n1 and n3 > n2:
    print(n1,"é maior número.")

elif n2 == n3 and n2 and n3 > n1:
    print(n2,"é maior número.")        
