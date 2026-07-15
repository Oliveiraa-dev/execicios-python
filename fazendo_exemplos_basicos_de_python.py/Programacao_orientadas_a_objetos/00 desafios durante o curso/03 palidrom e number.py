"""
Dado um número inteiro x, retorne truese xfor umpalíndromoe falsede outra forma .

 

Exemplo 1:

Entrada: x = 121
 Saída: verdadeiro
 Explicação: 121 lê-se como 121 da esquerda para a direita e da direita para a esquerda.
Exemplo 2:

Entrada: x = -121
 Saída: falso
 Explicação: Da esquerda para a direita, lê-se -121. Da direita para a esquerda, torna-se 121-. Portanto, não é um palíndromo.
Exemplo 3:

Entrada: x = 10
 Saída: falso
 Explicação: Lê-se 01 da direita para a esquerda. Portanto, não é um palíndromo.
 

Restrições:

-231 <= x <= 231 - 1
 

Pergunta complementar: Você conseguiria resolver isso sem converter o número inteiro em uma string?
"""

class Solution: 
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        original = x
        invertido = 0

        while x > 0:

            ultimo = x % 10

            x = x // 10

            invertido = invertido * 10 + ultimo

    
        return original == invertido