def e_primo(n):
    if n <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    if n % 2 == 0:
        return False
    # Verifica se o número é divisível por algum número além de 1 e ele mesmo
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False  # Se encontrar um divisor, não é primo
        divisor += 2  # Avança para o próximo número ímpar
        return True  # Se não encontrar nenhum divisor, é primo

# Exemplos de uso:
print(e_primo(2))  # True
print(e_primo(17))  # True
print(e_primo(15))  # False
