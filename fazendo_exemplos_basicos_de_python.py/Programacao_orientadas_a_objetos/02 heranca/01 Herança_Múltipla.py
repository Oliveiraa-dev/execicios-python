class animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class mamifero(animal):
    def __init__(self, num_patas, cor_pelo):
        self.num_patas = num_patas
        self.cor_pelo = cor_pelo
        super().__init__(num_patas)

class ave(animal):
    def __init__(self, num_patas):
        self.num_patas = num_patas
        super().__init__(num_patas)

class cachorro(mamifero):
    pass


class gato(mamifero):
    pass


class onitorrinco(mamifero, ave):
    pass


gato = gato(4, "escuro " )
print(gato)

onitorrinco(4,)