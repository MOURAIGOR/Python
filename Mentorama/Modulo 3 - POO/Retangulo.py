class Retangulo:
    # Atributos
    def __init__(self, comprimento, altura):
        self.setcomprimento(comprimento)
        self.setAltura(altura)
    # Métodos
    def setcomprimento(self, comprimento):
        self.comprimento = comprimento

    def getcomprimento(self):
        return self.comprimento

    def setAltura(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura

    def calculaArea(self):
        return self.comprimento * self.altura

    def calculaPerimetro(self):
        return 2 * self.comprimento + 2 * self.altura

# Executando
comprimento = int(input('Valor do comprimento: '))
altura = int(input('Valor da altura: '))
retangulo = Retangulo(comprimento, altura)
print('A area do retangulo é: %d' % retangulo.calculaArea())
print('O perimetro do retangulo é : %d' % retangulo.calculaPerimetro())
