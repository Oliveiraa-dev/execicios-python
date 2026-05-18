class passaro:
    def voar(self):
        print("voando...")


class pardal(passaro):
    def voar(self):
        super().voar()

class Avestruz(passaro):
    def voar(self):
        print("Avestruz nao pode voar")

def plano_voo(obj):
     obj.voar()

p1 = pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)