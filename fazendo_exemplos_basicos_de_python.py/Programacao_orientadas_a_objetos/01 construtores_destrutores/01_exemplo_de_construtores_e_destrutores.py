class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("removendo a instancia da classe")

    def falar(self):
        print("uauuu..uauuuuu")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto", False)
    print(c.nome)

c = Cachorro("chapie", "amarelo")
c.falar()

criar_cachorro()

