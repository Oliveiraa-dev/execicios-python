


# __unit__ construtor

class cachorro:
 def __unit__(self, nome, cor, acordado=True):
    self.nome = nome
    self.cor = cor
    self.acordado = acordado
    
    #  o termo ( __unit__ ) rerefe a construir uma classe


# __del__ destrutor

class cachorro:
  def __del__(self):
    print("destruindo a instancia")


c = cachorro()
del c