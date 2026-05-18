class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
      print("ligando o motor")

    def __str__(self):
        return f"Veículo {self.cor} - placa {self.placa} - {self.numero_rodas} rodas"



class motocicleta(Veiculo):
        pass

class carro(Veiculo):
        pass

class caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado):
         super().__init__(cor, placa, numero_rodas)
         self.carregado = carregado
    
    def estar_carregado(self):
         print(f"{'sim' if self.carregado else 'nao'} estou carregado..")




moto = motocicleta("vermelha", "aidento-157", 2)

carro = carro("branco", "aidento-171",4 )

caminhao = caminhao("rosa", "aidento-007", 8, True)

print(moto)
print(carro)
print(caminhao)
