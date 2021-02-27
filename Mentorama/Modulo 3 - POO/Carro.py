# crie uma classe carro.
# min 3 propriedade e metodos, sendo que um dos metodos e para imprimir todos os dados do carro
#  a) crie 3 obj. para carros diferentes que recebem  como entrada o parametros
# das propri. que definiu
#  b) consulte cada um desses parame. para cada um objeto criando no execicio anterior
#  c) chame cada um desses para. cridados para verficar o correro fun.

class Carro:
    def __init__ (self, marca= "", ano= 0000, tipo= "" ):
        self.marca = marca
        self.ano = ano
        self.tipo = tipo
        self.velocidade = 0

    def ligar(self):
        print("Ligado")

    def buzinar(self):
        print("Bi-bi, Bi-bi")

    def acelerar(self):
        self.velocidade += 5
        print("Você esta acelerando, sua velociade atual é: {} ".format(self.acelerar))


Fusca = Carro("Volkswagen", 1986, "Conversível")

Fusca.ligar()
Fusca.buzinar()
Fusca.acelerar()

Fusca.velocidade()


