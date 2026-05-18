maior_idade = 18
idade_especial = 12
idade = int(input("informe sua idade: "))

  # usando apenas a condicao IF

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH.")

if idade < maior_idade:
    print("ainda nao pode tirar a CNH.")  

 # usando a condicao IF, ELSE

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH.")

else:
    print("ainda nao pode tirar a CNH.")   

 #  # uando a condicao IF, ELIF E ELSE

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH.")

elif idade == idade_especial:
    print("pode fazer as aulas teoricas, mas nao pode fazer as praticas.")

else:
    print("ainda nao pode tirar a CNH.")   






