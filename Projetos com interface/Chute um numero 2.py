import random


class ChuteoNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarValorAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Você errou!!! Dica: É um número menor.')
                    self.PedirValorAleatorio()
            
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Você errou!!! Dica: É um número maior.')        
                    self.PedirValorAleatorio()    
        
                if int(self.valor_do_chute) == self.valor_aleatorio:    
                    self.tentar_novamente = False
                    print('Ebaaa!!! Você acertou o numero')
        except:
            print('Por favor digite apenas números')
            
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarValorAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteoNumero()
chute.Iniciar()
