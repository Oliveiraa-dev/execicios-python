class Solution:
    def romanToInt(self, s: str) -> int:

        valores = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        resultado = 0

        for i in range(len(s)):
            atual = valores[s[i]]

            if i < len(s) - 1:
                proximo = valores[s[i + 1]]

                if atual < proximo:
                    resultado -= atual
                else:
                    resultado += atual
            else:
                resultado += atual

        return resultado

print(Solution().romanToInt("MCMXCIV"))