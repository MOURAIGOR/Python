class televisao:
    #Atributos
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    #Metodos     
    def trocar_canal(self, canal):
        if self.canal >= 100:
            print("Canal bloquado ligue para central")
        
        else:
            a_ch = canal + self.canal
            self.canal = a_ch
            print('****CANAL {} ****'.format(a_ch))
        

    def trocarCanal(self, canal):
        if (self.canal <= 0):
            print('***********')
        
        else:
           d_ch = self.canal - canal
           self.canal = d_ch 
           print('**** CANAL {} **** '.format(d_ch))
 
    def aumetar_volume (self, volume):
        if self.volume >= 100:
            print('Volume Maximo')

        else:
            a_vol = volume + self.volume
            self.volume = a_vol
            print('Volume {}'.format(a_vol))

    def baixar_volume(self, volume):
        if self.volume <= 0:
            print('Mudo')

        else:
            d_vol = self.volume - volume
            self.volume = d_vol
            print('Volume {}'.format(d_vol))

#executando
def main ():
    tv = televisao( 0, 0)
    resposta = ''
    
# ch+ = avançar para proximo canal
# ch- = voltar para o canal anterior
# vol+ = aumeta o volume
# vol- = abaixa o volume
# Deligar = desliga a tv
    while(resposta != '5'):
        resposta = str(input('1 Ch+, 2 Ch-, 3 Vol+, 4 Vol-, 5 Deligar: '))

        if (resposta == '1'):
            a_ch = 1
            tv.trocar_canal(a_ch)

        elif  (resposta == "2"):
            d_ch = 1     
            tv.trocarCanal(d_ch)

        elif(resposta == "3"):
            a_vol = 5
            tv.aumetar_volume(a_vol)

        elif(resposta == "4"):
            d_vol = 5
            tv.baixar_volume(d_vol)    
main()      








