"""
Desafio 1 - Sistema de Pontuação (Nível RomanToInt)
Problema

Em um jogo, cada letra representa uma quantidade de pontos.

Letra	Pontos
A	1
B	5
C	10
D	50

Você receberá uma String.

Exemplo:

"ABCD"

Você deve calcular a pontuação seguindo esta regra:

Se a próxima letra tiver um valor MAIOR que a atual, subtraia.
Caso contrário, some.
"""

#    ESQUELETO DO ALGORITMO

class Solution:

    def calcularPontos(self, s: str) -> int:

        pontos = {
            'A':1,
            'B':5,
            'C':10,
            'D':50
        }

        resultado = 0

        # ESCREVA O RESTANTE :

        for i in range(len(s)):
            Letra_atual = pontos[s[i]]

            if i < len(s) - 1:
                proximo = pontos[s[i + 1]]

                if Letra_atual < proximo:
                    resultado -= Letra_atual

                else:
                    resultado += Letra_atual

            else:
                resultado += Letra_atual


        return resultado
    
print(Solution().calcularPontos("AB"))