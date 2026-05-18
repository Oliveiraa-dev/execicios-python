#USANDO MAIÚSCULO, MINÚSCULOO E TÍTULO

nome = "marllon"

print(nome.upper()) # deixa tudo em maiúsculo
print(nome.lower()) # deixa tudo em minúsculo
print(nome.title()) # deixa a primeira letra em maiúsculo


#ELIMINANDO ESPACOES EM BRANCOS

nome = "    nayane  "

print(nome.strip()) # tira espacos em branco na direita e esquerda
print(nome.lstrip()) # tira espacos em branco na ESQUERDA
print(nome.rstrip()) # tira espacos em branco na DFIREITA

#juncoes e centralizacao

nome= "fernandes"

print(nome.center(25, " ")) # completa espacos mem branco com o que vc tenha escolhido colocar no lugar
print(" ".join(nome)) # coloca o que voce escolheu para separar cada letra