class Retangulo:
    def __init__(self, comprimento = "0", largura = "0"):
        self.comprimento = comprimento
        self.largura = largura

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento (self, valor):

        if valor.isdigit():
            self.__comprimento = valor

        else:
            print("Insira apenas numeros")

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, valor):

        if valor.isdigit():
            self.__largura = valor

        else:
            print("Insira apenas numeros")

    def mudarValor(self):
        C = input("\nCompromento: ")
        self.comprimento = C

        L = input("\nLargura: ")
        self.largura = L

    def mostrarValor(self):
        print("\n--- Retangulo ---")
        print("Comprimento: {}".format(self.comprimento))
        print("Largura: {}".format(self.largura))
        print("-------------------")

    def calcArea(self):
        print("\nA área do retangulo é {} m2".format(float(self.__comprimento) * float(self.__largura)))
   
    def caclPerimetro(self):
        print("O perimetro é {} m2".format((float(self.__comprimento) * 2 ) + (float(self.__largura)* 2)))

def main():
    r = Retangulo()
    r.mostrarValor()
    
    r.mudarValor()
    r.mostrarValor()

    r.calcArea()
    r.caclPerimetro()

main()             
