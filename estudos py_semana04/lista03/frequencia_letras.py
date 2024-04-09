from collections import Counter

# Lendo o número de casos de teste
N = int(input())

# Processando cada caso de teste
for _ in range(N):
    # Lendo a linha de texto e convertendo para minúsculas
    linha = input().lower()

    # Inicializando um contador para contar a frequência das letras
    freq_letras = Counter()

    # Contando a frequência das letras
    for letra in linha:
        if letra.isalpha():
            freq_letras[letra] += 1

    # Encontrando a maior frequência
    max_freq = max(freq_letras.values())

    # Inicializando uma lista para armazenar as letras de maior frequência
    letras_max_freq = []

    # Iterando sobre as letras e suas frequências
    for letra, freq in freq_letras.items():
        if freq == max_freq:
            letras_max_freq.append(letra)

    # Ordenando as letras de maior frequência em ordem alfabética
    letras_max_freq.sort()

    # Imprimindo as letras de maior frequência em ordem alfabética
    print(''.join(letras_max_freq))
