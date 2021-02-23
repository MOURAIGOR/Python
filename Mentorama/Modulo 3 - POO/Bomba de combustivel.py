class Bomba_de_combustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.quantidadeCombustivel = quantidadeCombustivel
        self.valorLitro = valorLitro

    def abastecerPorValor(self, valorpago):
        qtdlitros = valorpago / self.valorLitro
        self.quantidadeCombustivel = self.quantidadeCombustivel + (qtdlitros)
        print("Deu total de %.2f litros" % qtdlitros)

    def abastecerPorLitro(self, quantidadeLitro):
        valorPago = quantidadeLitro * self.valorLitro
        self.quantidadeCombustivel = self.quantidadeCombustivel + quantidadeLitro
        print("Deu total de R$ %.2f " % valorPago)

    def alterarCombustivel(self, combustível):
        self.tipoCombustivel = combustível
        return self.tipoCombustivel

    def alterarQuantidadeCombustivel(self, Novaquantidade):
        self.quantidadeCombustivel = Novaquantidade
        print('A quantidade é  %.2f litros' %Novaquantidade)

    def alterarValor(self, novoPreço):
        self.valorLitro = novoPreço
        print("Preço alterado para R$ %.2f" %novoPreço)


def main():
    bomba01 = Bomba_de_combustivel('Gasolina', 3.99, 2.000)
    bomba02 = Bomba_de_combustivel('Etanol', 2.59, 1.500)
    bomba03 = Bomba_de_combustivel('Disiel', 4.00, 1.000)
    resp = ''

    resp = str(input("Vai abastecer com Gasolina, Etanol , Disiel ou Sair: "))
    while (resp != 'Sair'):
        if (resp == 'Gasolina'):
            resp2 = str(
                input('*Abastecer por : litro , preço. ,*alterar preço , *alterar quantidade: '))
            if (resp2 == "litro"):
                qtdlitros = float(input("Quantos litros vai abastecer?  "))
                bomba01.abastecerPorLitro(qtdlitros)

            elif (resp2 == "preço"):
                valorPago = float(input('Qual o valor que vai abatecer? '))
                bomba01.abastecerPorValor(valorPago)

            elif (resp2 == 'alterar preço'):
                novoPreço = float(input('Digite o novo preço: '))
                bomba01.alterarValor(novoPreço)

            elif (resp2 == 'alterar quantidade'):
                Novaquantidade = float(input('Digite a nova quantidade: '))
                bomba01.alterarQuantidadeCombustivel(Novaquantidade)

            else:
                print('Digite apenas as fornecidas')

        elif (resp == 'Etanol'):
            resp2 = str(
                input('*Abastecer por: litro, preço., *alterar preço, *alterar quantidade:  '))
            if (resp2 == "litro"):
                qtdlitros = float(input("Quantos litros vai abastecer?  "))
                bomba02.abastecerPorLitro(qtdlitros)

            elif (resp2 == "preço"):
                valorPago = float(input('Qual o valor que vai abatecer? '))
                bomba02.abastecerPorValor(valorPago)

            elif (resp2 == 'alterar preço'):
                novoPreço = float(input('Digite o novo preço: '))
                bomba02.alterarValor(novoPreço)

            elif (resp2 == 'alterar quantidade'):
                Novaquantidade = float(input('Digite a nova quantidade: '))
                bomba02.alterarQuantidadeCombustivel(Novaquantidade)

            else:
                print('Digite apenas as fornecidas')

        elif (resp == 'Disiel'):
            resp2 = str(
                input('*Abastecer por: litro, preço., *alterar preço, *alterar quantidade:  '))
            if (resp2 == "litro"):
                qtdlitros = float(input("Quantos litros vai abastecer?  "))
                bomba03.abastecerPorLitro(qtdlitros)

            elif (resp2 == "preço"):
                valorPago = float(input('Qual o valor que vai abatecer? '))
                bomba03.abastecerPorValor(valorPago)

            elif (resp2 == 'alterar preço'):
                novoPreço = float(input('Digite o novo preço: '))
                bomba03.alterarValor(novoPreço)

            elif (resp2 == 'alterar quantidade'):
                Novaquantidade = float(input('Digite a nova quantidade: '))
                bomba03.alterarQuantidadeCombustivel(Novaquantidade)

            else:
                print('Digite apenas as fornecidas')
main()