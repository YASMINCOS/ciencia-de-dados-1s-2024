# for in

notas = [8,9,10]

for nota in notas:
    print(nota)

notas_dic ={
    "alice": 9,
    "bob": 10,
    "carlos ": 6
}

for n in notas_dic:
    print(n)
    print(notas_dic[n])

for n in notas_dic.items():
    print(n)

for k,v in notas_dic.items():
    print(k, v)