class Pessoa:
    #Atributos
    def __init__(self, nome="Pessoa", idade=0 , altura=0.0 , peso=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    #Metodos
    def crescer(self, cm):
        
        self.altura += cm / 100
        print("{} cresceu {} cm, e agora tem {:.3f} m de altura".format(self.nome, cm, self.altura))

    def engordar(self, kg):
        self.peso += kg
        print("{} você engordou {}kg, agora seu peso atual é {}kg".format(self.nome, kg, self.peso))

    def emagrecer(self, kg):
        self.peso -= kg
        print("{} você emagreceu {}kg, agora seu peso atual é {}kg".format(self.nome, kg, self.peso)) 

    def envelhercer (self, anos):
        cresc = 0 

        if self.idade + anos <= 21:
            cresc = anos * 0.5

        if self.idade < 21:
            if self.idade + anos > 21:
                cresc = ((21 - self.idade) * 0.5)

        self.idade += anos

        print("{} agora você está com {} anos de idade".format(self.nome, self.idade))
        self.crescer(cresc) 

#executando
def main():
    Lucas = Pessoa("Lucas", 21, 1.50, 65)

    print("A altura do {}: é {} cm".format(Lucas.nome, Lucas.altura))
    Cr = int(input("O quanto deseja crescer? (cm): "))
    Lucas.crescer(Cr)

    print()

    print("O peso do {}: é {} kg".format(Lucas.nome, Lucas.peso))
    Pe = int(input("O quanto deseja engorgar: (kg): "))
    Lucas.engordar(Pe)

    print()

    print("O peso do {}: é {} kg".format(Lucas.nome, Lucas.peso))
    Em = int(input("O quanto deseja emagrecer: (kg): "))
    Lucas.emagrecer(Em)

    print()

    print("A idade do {}: é {} cm".format(Lucas.nome, Lucas.idade))
    An = int(input("O quanto deseja envelhecer? (idade): "))
    Lucas.envelhercer(An)

    print()

main()   
