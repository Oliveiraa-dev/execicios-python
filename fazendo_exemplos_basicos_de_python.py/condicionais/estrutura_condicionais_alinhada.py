conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:

        print("saque realizado com sucesso!.")

    elif saque <= (saldo + cheque_especial):

        print("saque realizado com uso de cheque especial!")

    else:

        print("nao foi possivel realizar o saque, saldo insuficiente!.")

elif conta_universitaria:

    if saldo>= saque:

        print("saque realizado com sucesso!")

    else:

        print("saque insuficiente!")

else:
    
    print("sistema nao reconheceu o tipo de conta!, entre em contato com o gerente")