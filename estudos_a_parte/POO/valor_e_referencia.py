notas_originais = [3,2,8]
notas_ordenadas = sorted(notas_originais)

print("Ordenadas" , notas_ordenadas)
print("Originais" , notas_originais)

"""o sorted cria enderecamentos diferentes em memoria,
 diferente no sort
 Funncao com efeiro colaterial"""

def faz_alguma_coisa(lista):
    ...
    lista.append(8)
    ...

lista1 = [1,2,3] #mutavel
#tupla e imutavel
x = faz_alguma_coisa(lista1)
print(lista1)
