usuarios = { "alice", "bob", "carlos"}

usuarios_2 = set(["alice", "bob", "lucas"])

print(usuarios == usuarios_2)

print(usuarios)
usuarios.add("bob")
#nao permite elementos repitidos e nao garante a ordenacao de insercao de elementos
print(usuarios)

#calculos matematicos
print(usuarios.union(usuarios_2))
print(usuarios.intersection(usuarios_2))
print(usuarios.difference(usuarios_2))
print(usuarios_2.difference(usuarios))


#e_igual = usuarios.union(usuarios_2) == usuarios | usuarios_2
#e_igual = usuarios.difference(usuarios_2) == usuarios - usuarios_2

e_igual = usuarios.intersection(usuarios_2) == usuarios & usuarios_2
print(e_igual)