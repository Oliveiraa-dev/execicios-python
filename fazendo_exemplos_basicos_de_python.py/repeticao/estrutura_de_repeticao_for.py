texto = input("informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:

    print()
    print("executa no final do laco") # adicona uma quebra de linha

    # exemplo utilizando a funcao built-in range
    for numero in range(0, 51, 5):
        print(numero, end=" ")