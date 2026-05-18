nome = "Nayane"
idade = 22
profissao = "analista de qualidade"
curso = "estetica e cosmetica"
saldo = 195.50

dados = {"nome": "Nayane", "idade": 22}

print("nome : %s idade: %d" % (nome, idade))
print("nome : {} idade: {}".format (nome, idade))
print("nome : {0} idade: {1}".format (nome, idade))
print("nome : {0} idade: {1} nome: {0} {0}".format (nome, idade))
print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("nome: {name} idade: {age} {name} {age} {age}".format(age=idade, name=nome))
print("nome: {nome} idade: {idade}".format(**dados) )

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.1f}")