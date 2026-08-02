""" Prefixo comum mais longo
dificuldade: Fácil
Empresas
Escreva uma função para encontrar a string com o prefixo comum mais longo em um array de strings.

Se não houver um prefixo comum, retorne uma string vazia "".

Exemplo 1:

Entrada: strs = ["flower","flow","flight"]
 Saída: "fl"

Exemplo 2:

Entrada: strs = ["dog","racecar","car"]
 Saída: ""
 Explicação: Não há prefixo comum entre as strings de entrada.
 

Restrições:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i]Consiste apenas em letras minúsculas do alfabeto inglês, caso não esteja vazio.
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:

    for i in range(len(strs[0])):

        for palavra in strs[1:]:

            if i >= len(palavra) or palavra[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))