class trabalhador_CLT :
    empresa = "moura&CIA"
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario\
        
    def __str__(self):
        return f"{self.nome}, {self.matricula}, {self.salario}, {self.empresa}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

clt_1 = trabalhador_CLT("marllon", 32272, 2500)
clt_2 = trabalhador_CLT("nayane", 1234, 3000)
mostrar_valores(clt_1, clt_2)

clt_1.matricula = 30001   # exemplo atributo de estância
mostrar_valores(clt_1, clt_2)

trabalhador_CLT.empresa = "oliveira&CIA" # exemplo atributo de classe
mostrar_valores(clt_1, clt_2)
