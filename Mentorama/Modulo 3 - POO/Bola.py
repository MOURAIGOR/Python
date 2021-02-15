class Ball: 
    def __init__(self, color="", circunf=0, material=""):
        self.color = color
        self.circunf = circunf
        self.material = material

    def troca_Cor(self):
        troca = input("Deseja mudar a cor atual {}? [s/n]".format(self.color))
        
        
        troca = troca[0].lower()        

        if troca == "s":
            nova_cor = input("\n> Nova Cor: Branco ")
            self.color = nova_cor

        else:
            print("Ok, a cor continua {}".format(self.color))

    def mostrar_Cor(self):
        print("\n A cor atual é {}".format(self.color))

def main():
    bola01 = Ball("Azul", 5, "Borracha") 

    while True:
        bola01.mostrar_Cor() 
        bola01.troca_Cor()
        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()

        if continuar == "n":
            break
                    
    bola01.mostrar_Cor()

main()


                     
