class Quadrado:
    def __init__(self, lado):
        self.tamanho_lado = lado

    def mudar_valor_lado(self, novo_lado):
        lado = novo_lado
        self.tamanho_lado = novo_lado

    def retornar_valor_lado(self, retorno):
        self.tamanho_lado = retorno
        print(retorno)

    def calcular_area(self, area):
        self.tamanho_lado = area
        print(area*area)

quadrado = Quadrado(6)
print('Tamanho atual é:')
print(quadrado.tamanho_lado)
print('----------------')
quadrado.mudar_valor_lado(3)
print('Novo tamanho é:')
print(quadrado.tamanho_lado)
print('----------------')
print('Tamanho atual:')
quadrado.retornar_valor_lado(3)
print('----------------')
print('Total da area ficou em :')
quadrado.calcular_area(3)
