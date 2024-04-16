import numpy as np

'''''arrays  - conjunto de dados '''
#nadarray - arrays de complexas dimensoes 

#criando um array
a = np.array([[1,2,3,4,5,6], [1,4,5,67,8,7]])
print(a)

#shape: 5 de tamanho, 3 de linhas e 6 de colunas
zero_array = np.zeros(shape = (5,3,6))
print(zero_array)

um_array = np.ones((2,3))
print(um_array)

vazio = np.empty(2)
print(vazio)  

arr = np.arange(10)
print(arr)

#comecando entre valores diferentes
arra_arange = np.arange(50,200,30)
print(arra_arange)

numeros = np.array([2,3,4,5,6,7,8,9], np.int16)
print(type(numeros))
print(numeros)
print(numeros[0])
print(numeros.dtype)

#Array bidimensionais com Numpy
M = np.array([[1,3,5],[2,4,6],[3,5,7]])
print(M)
print('Primeira coluna: ', M[:,0])
print('Segunda coluna: ', M[:,1])
print('Terecira coluna: ', M[:,2])