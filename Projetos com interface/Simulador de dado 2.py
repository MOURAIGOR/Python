Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
import PySimpleGUI as sg


class simulador_de_dado():
    def __init__(self):
        self.valor_maximo = 6
        self.valor_minimo = 1 
        
        #LAYOUT
        self.layout = [
            [sg.Text('Jogar o dado ? ')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
        
    def inicio(self):
        #CRIAR UMA JANELA
        self.janela = sg.Window('Simulador de dados', layout=self.layout)

        #LER VALORES DA TELA
        self.eventos, self.valores = self.janela.Read()
        
        #FAZER ALGO COM OS ESSES VALORES 
        
        try:
            if self.eventos == 'Sim' or self.eventos == 'S':
                self.gerar_valor()
            
            elif self.eventos == 'Não' or self.eventos == 'N':
                print('Ok, obrigado pela participação')
            
            else:
                print('Por favor digite apenas sim ou não')
        except:
            print('Desculpe não consegui entender sua resposta')

    def gerar_valor(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))        

simulador = simulador_de_dado()
simulador.inicio()
© 2021 GitHub, Inc.