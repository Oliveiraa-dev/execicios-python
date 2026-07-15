class Pessoa:
    def __init__(self,nome=None, idade=None):
        self.nome = nome 
        self.idade = idade

    # Metodo de classe:
    # - usa o decorador @classmethod;
    # - recebe a propria classe como primeiro parametro, por convencao chamado cls;
    # - e usado quando o metodo precisa criar ou alterar algo relacionado a classe;
    # - aqui ele cria uma Pessoa a partir da data de nascimento.
    @classmethod

    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        # cls(nome, idade) chama o construtor da classe Pessoa.
        # Assim, o metodo devolve um novo objeto Pessoa ja preenchido.
        return cls(nome, idade)
    
    # Metodo estatico:
    # - usa o decorador @staticmethod;
    # - nao recebe self nem cls automaticamente;
    # - funciona como uma funcao comum, mas fica organizada dentro da classe;
    # - use quando a regra tem relacao com a classe, mas nao precisa acessar o objeto.
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
# Objeto criado do jeito tradicional, chamando Pessoa(...) diretamente.
p = Pessoa("marllon", 22)
print(p.nome, p.idade)

# Objeto criado pelo metodo de classe.
# Mesmo sendo chamado por uma instancia, o ideal e chamar pela classe:
# Pessoa.criar_apartir_data_nascimento(...)
p2 =  Pessoa().criar_apartir_data_nascimento(2003, 4, 7, "marllon")
print(p2.nome, p2.idade)

# Chamando o metodo estatico direto pela classe.
# Ele apenas valida a idade recebida e retorna True ou False.
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
