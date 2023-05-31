class Brow:
  def __init__(self, nome, sexo, idade,comida, acordado = False, fome = False, sujo = False,apaixonado= False):
    self.nome = nome
    self.sexo = sexo
    self.idade = idade
    self.comida = comida
    self.acordado = acordado
    self.fome = fome
    self.sujo = sujo
    self.apaixonado = apaixonado

  
  def apresentar(self):
    if self.acordado == False:
      print(f'O Brow {self.nome} está dormindo, você precisa acorda-lo\n(￣﹃￣) !')
    else:
      print(f'O Brow {self.nome} já está acordado, dê os comandos ╰(*°▽°*)╯ !')

  def acordar(self):
    self.acordado = True
    self.sujo = True
    self.fome = True
    
    if self.acordado == True:
      print(f'Olá, me chamo {self.nome}, tenho {self.idade} anos e estou extremamente com fome e sujo ╰(*°▽°*)╯\ntenha piedade e me dê comida e um bom banho ヽ（≧□≦）ノ!!!')

  def dormir(self):
    self.acordado = False
    if self.acordado == False:
      print(f'O {self.nome} foi dormir ...\n(✿◡‿◡) ~zZzZzZZzZz')

  def comer(self):
    if self.acordado == True:
      self.fome = True
      print(f'O {self.nome} está faminto e agora está comendo uma deliciosa {self.comida}\n（＾∀＾●）ﾉｼ. ~nhaamNhaaaamm')
    else:
      print(f'O {self.nome} não pode comer, pois está dormindo\n(✿◡‿◡) ~ZzZZzZzZzzZ')

  def banho(self):
    if self.acordado == False or self.sujo == False:
      print(f'{self.nome} não pode tomar banho, pois está dormindo\nAcorde-o')
    else:
      print(f'{self.nome} está tomando um delicioso banho de banheira\n╰(*°▽°*)╯ ~Agora está limpo e cheiroso !!!')

  def apaixonar(self):
    self.apaixonado = True
    print('Ops, Zé se encantou em um cangote\nisso é amor no ar?\n❤ ❤ ❤ ❤❤ ❤ ❤ ❤❤ ❤ ❤ ❤ ')
  
  def amar(self):
    if self.apaixonado == False:
      print(f'{self.nome} não está afim de namorar, deixe-o curtir a solteirisse !!! ¯\_( ͡° ͜ʖ ͡°)_/¯')
    else:
      print(f'{self.nome} está apaixonado ❤ ❤ ❤ ❤\n (❤ ω ❤)/ \（＞人＜；）')
