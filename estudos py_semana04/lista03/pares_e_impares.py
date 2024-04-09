# Lendo o número de linhas
N = int(input())

# Inicializando listas para números pares e ímpares
pares = []
impares = []

# Lendo os números e separando pares e ímpares
for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Ordenando as listas
pares.sort()
impares.sort(reverse=True)

# Imprimindo os números
for par in pares:
    print(par)
for impar in impares:
    print(impar)


""""O `_` é uma convenção em Python para indicar uma variável que não será usada no loop. É comumente usado quando você não precisa dos valores dos elementos do iterável, mas apenas precisa iterar sobre eles. Nesse caso específico, usamos `_` no loop `for` porque não precisamos dos valores das linhas adicionais de entrada (além do número total de linhas `N`). Estamos apenas iterando `N` vezes para ler essas linhas e não fazemos uso dos valores nelas contidos.

Então, o `_` é uma maneira de indicar explicitamente que não estamos usando os valores das linhas adicionais, apenas iterando sobre elas para leitura e processamento. Isso ajuda a tornar o código mais claro para quem o está lendo, indicando que os valores não são relevantes para a lógica do programa."""