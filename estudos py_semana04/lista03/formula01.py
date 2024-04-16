def calcular_pontos(resultados, sistema_pontuacao):
    pontos = [0] * len(resultados[0])  # Inicializa a lista de pontos de cada piloto como zeros
    
    for corrida in resultados:
        for i, posicao in enumerate(corrida):
            if posicao <= len(sistema_pontuacao):
                pontos[i] += sistema_pontuacao[posicao - 1]  # Adiciona os pontos de acordo com a posição na corrida
    
    return pontos

def identificar_campeao(pontuacoes):
    maior_pontuacao = max(pontuacoes)
    campeoes = [i + 1 for i, pontuacao in enumerate(pontuacoes) if pontuacao == maior_pontuacao]
    return campeoes

while True:
    G, P = map(int, input().split())
    if G == 0 and P == 0:
        break
    
    resultados = [list(map(int, input().split())) for _ in range(G)]
    S = int(input())
    for _ in range(S):
        k, *sistema_pontuacao = map(int, input().split())
        pontuacoes = calcular_pontos(resultados, sistema_pontuacao)
        campeoes = identificar_campeao(pontuacoes)
        print(*campeoes)


"""

1. **Definição das Funções**:
   - `calcular_pontos(resultados, sistema_pontuacao)`: Esta função recebe os resultados de cada corrida e um sistema de pontuação específico. Ela itera sobre cada corrida e para cada posição de chegada em cada corrida, adiciona os pontos correspondentes do sistema de pontuação ao piloto. Ao final, retorna uma lista contendo a pontuação total de cada piloto.
   - `identificar_campeao(pontuacoes)`: Esta função recebe a lista de pontuações totais de cada piloto. Ela determina a maior pontuação obtida por um piloto e retorna uma lista contendo os identificadores dos pilotos que alcançaram essa pontuação máxima.

2. **Entrada de Dados**:
   - O programa começa com um loop que continua até que seja fornecido um caso de teste com 0 para o número de Grandes Prêmios e 0 para o número de pilotos.
   - Para cada caso de teste, o programa lê G (o número de Grandes Prêmios) e P (o número de pilotos) da entrada.
   - Em seguida, lê os resultados de cada corrida e armazena-os em uma lista de listas chamada `resultados`.
   - Então, lê o número de sistemas de pontuação, S.
   - Para cada sistema de pontuação, o programa lê a descrição do sistema e chama a função `calcular_pontos()` para calcular as pontuações dos pilotos com base nesse sistema de pontuação.
   - Depois, chama a função `identificar_campeao()` para identificar os campeões mundiais de pilotos para o sistema de pontuação atual e imprime os resultados correspondentes.

3. **Cálculo dos Pontos**:
   - A função `calcular_pontos()` itera sobre cada corrida e para cada posição de chegada em cada corrida, adiciona os pontos correspondentes do sistema de pontuação ao piloto.

4. **Identificação do Campeão**:
   - A função `identificar_campeao()` determina a maior pontuação obtida por um piloto e retorna uma lista contendo os identificadores dos pilotos que alcançaram essa pontuação máxima.

5. **Saída**:
   - O programa imprime os identificadores dos campeões mundiais de pilotos para cada sistema de pontuação.

Este é o fluxo principal do programa, onde ele lê os dados, realiza os cálculos e emite os resultados para cada caso de teste."""



#soloucao feita em sala

"""""
while True:

"""

while True:
   l1 = input().split()
   G = int(l1[0])
   if G ==0:
       break
   
   P = int(l1[1])
   tabela = []
   
   for i in range(G):
       corrida =[]
       l2 = input().split()
       for j in range(P):
           corrida.append(int(l2[j]))
       tabela.append(corrida)
     
   S = int(input())
   for i in range(S):
       l3 = input().split()
       pos = int(l3[0])
       pontos =[]
       for j in range(pos):
           pontos.append(int(l3[j + 1]))
       pontosPilotos = [0] *P
       
       for c in tabela:
           for j in range(P):
               if c [j] <= pos:
                   pontosPilotos += pontos[c[j ]- 1]
                   
        maxp = max(pontosPilotos)  
        flag = False         
        for j in range(P):
            if pontosPilotos[j] == maxp;
              if flag:
                  print()
            print(j+1)     
            flag = True  
        
           