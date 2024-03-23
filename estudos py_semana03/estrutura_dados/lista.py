notas = [8, 10 , 8.5]
#       0    1    2
#adicionar elemento no final da lista
notas.append(9)
print(notas[3])

#ordennar notas
notas.sort(reverse= True)
print(notas)

notas.pop()
print(notas)

notas.insert(0,8)
print(notas)



pessoas = [
    ["Yasmin", 21 , "223333"],
    ["Maria", 12 , "5554"]
]

notas_novo = [8,9,10, 7.5, 4, 9]

i= 0
total = 0

qtd = len(notas_novo)
while i < qtd:
    total = total + notas_novo[i]
    i = i + 1

print(total)

media = total /5
print(media)
