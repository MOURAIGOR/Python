class conta_corrente:
    #atributos
    def __init__ (self, cliente, numero_conta, saldo):
        self.cliente = cliente
        self.saldo = saldo
        self.numero_da_conta = numero_conta 

    #Metodos 
    def sacar(self, valor):
        if(self.saldo < valor):
            print('*** Não tem saldo para saque! ***')

        else:
            self.saldo -= valor
            print('*** Foi sacado R${} da sua conta! ***'.format(valor))
            print('*** Seu saldo atual é R${} ***'.format(self.saldo))     

    def depositar(self, valor):
        if (valor <= 0):
            print('*** Não e possivel depositar esse valor! ***')
        
        else:
            self.saldo += valor
            print('\nO valor de R${} foi depositado com sucesso'.format(valor),)
            print(' \nO seu saldo atual é R${:.2f}'.format(self.saldo))

# executando 
def main():
    cliente01 = conta_corrente("João", 274313-2, 100)
    resposta = ''
    lista_de_opções = ['Depositar', 'Sacar', 'Consultar saldo', 'Sair']
    
    while (resposta != 'Sair'):
        resposta = str(input("Você deseja: *Depositar, *Sacar, *Consultar saldo ou *Sair: "))

        if(resposta == "Depositar"):
            valor = float(input("Digite o valor do deposito: "))
            cliente01.depositar(valor)

        elif(resposta == "Sacar"):
            valor = float(input('Digite o valor do saque: '))
            cliente01.sacar(valor)

        elif(resposta == "Consultar saldo"):
            print("O seu saldo da  sua conta {}".format(cliente01.numero_da_conta))
            print("O valor de  R${:.2f}".format(cliente01.saldo))
        
        elif(resposta not in lista_de_opções):
            print("Digite apenas as opções que estão na tela")
            print('Tente novamente ...')

main()
