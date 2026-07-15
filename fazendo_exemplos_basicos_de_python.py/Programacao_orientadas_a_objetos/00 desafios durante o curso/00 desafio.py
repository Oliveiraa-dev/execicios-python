# DESAFIO DO BICICLETARIO...

class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("fummmm..")
    
    def parar(self):
        print("parando bicicleta...")
        print("bicicleta parada...")
   
    def correr(self):
        print("vruuuummmmmmmm...")

   # def __str__(self):
   #     return f"bicicleta:{self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"


bike1 = bicicleta("vermelha", "monark", 2022, 1200)
bike1.buzinar()
bike1.correr()
bike1.parar()

bike2 = bicicleta("azul", "caloi", 2028, 15000)
bike2.buzinar() #bicicleta.buzinar(bike2)
print(bike2)

