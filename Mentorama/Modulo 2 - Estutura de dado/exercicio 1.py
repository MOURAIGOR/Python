# Crie um programa que leia o nome, sexo e idade de varias pessoas,guardando os dados em cada pessoa em um dic.
# e todos os dic. em uma lista. No final, moste:
#   A)quantas pessoas foram cadastradas
#   b) a media de idade
#   c) uma lista com as mulheres
#   d) uma lista de pessoas com idade acima da media

cadastro = list() #lista das pessoas cadastrada 
pessoas = dict() # dicionario de pessoas cadastradas 
soma = media = 0

# Obtenção de dados:
while True: 
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).upper()

    while True:
        pessoas['sexo'] = str(input('Sexo: ')).upper()
        if pessoas['sexo'] in 'MF':
            break
        print(f'Por favor, digite apenas M ou F')
    pessoas['idade']  = int(input('Idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Por favor digite apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)

# Realizando a analise dos dados obtidos:
print(f'A) A quantidade de pessoas cadastradas foram: {len(cadastro)}')
média  = soma / len(cadastro)
print(f'B) A media da idade foram: {média:5.2f} anos')
print(f'C) A(s) Mulher(es) cadastrada(s) são:')
for p in cadastro:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}')
print()        
print(f'D) lista de pessoas que estão com idade acima de media: ')
for p in cadastro:
    if p['idade'] >= média:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}')
    print()        

