from abc import ABC, abstractmethod


class controleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    def marca(self):
        pass

class controleTV(controleRemoto):
    def ligar(self):
        print("ligando a TV")
        print("ligada!")


    def desligar(self):
        print("desligando TV ...")
        print("desligada")

class controleArCondicionado(controleRemoto):
    def ligar(self):
        print("ligando o Ar Condicionado ...")
        print("ligada!")

    def desligar(self):
        print("desligando Ar Condicionado ...")
        print("desligada")



controle = controleTV()
controle.ligar()
controle.desligar()


controle = controleArCondicionado()
controle.ligar()
controle.desligar()