class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2003 - self._ano_nascimento
        

    

pessoa = Pessoa("marllon", 2003)
print(f"nome: {pessoa.nome} \tIdade: {pessoa.idade}")
print(f"nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")