valores_inteiros = []

for i in range(100):
    valor = int(input())
    valores_inteiros.append(valor)
    
maior = max(valores_inteiros)

#+ 1 pq a posicao comeca no zero
posicao_maior_valor = valores_inteiros.index(maior) + 1

print(maior)
print(posicao_maior_valor)