"""correcao professor"""
with open('teste1.txt', 'r') as f:
  n = int(f.readline())
  print(n)
  l = []
  for i in range(n):
    line = f.readline().split()
    l.append(line)
    print(line)
   
import numpy as np 

matriz = np.array(l)    
matriz = matriz.astype(int)

with open('saida.txt', 'w') as f:
  for x in [ 2, 3, 5, 7, 11]:
      resposta = np.sum(matriz % x == 0)
      f.write(f'{x}: {resposta}\n')
  f.close()