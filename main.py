from Brow import Brow
def l():
  print('-' * 85)

b1 = Brow('Ze','masculino',4,'Manga')
b2 = Brow('Nice','feminino',5,'Laranja')

#apresentando, inicialmente dormindo, sem sono e sem está sujo
b1.apresentar()
l()
#acordei, all bool = True
b1.acordar()
l()
#dormiu, all bool = False
b1.dormir()
l()
#eat, who eat?
b1.comer()
l()
#vamos acorda-lo novamente
b1.acordar()
l()
#hora de comer
b1.comer()
l()
#dormiu
b1.dormir()
l()
#tomar banho, mas tá dormindo
b1.banho()
l()
#acordar e tentar dar banho novamente
b1.acordar()
l()
#tomar banho
b1.banho()
l()
#apaixonar, mas ele não está afim, pois não está apaixonado
b1.amar()
l()
#vamos fazê-lo se apaixonar
b1.apaixonar()
#depois de apaixonado, agora pode amar
l()
b1.amar()
l()
l()
l()

b2.apresentar()
l()
b2.acordar()
l()
b2.banho()
l()
b2.comer()
l()
b2.amar()
#amar
l()
b2.apaixonar()
l()
b2.amar()
