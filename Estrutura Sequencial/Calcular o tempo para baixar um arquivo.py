arquivo = float(input("Informe o tamanaho do arquivo (MB): "))
velocidade = float(input("Informa a velicidade da internet (MBps): "))

tempo = arquivo / velocidade * 60

print("O tempo aprocimado de conclusao é: %.0f min" %tempo)
