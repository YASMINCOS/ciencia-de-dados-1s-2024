n = int(input())

listas = []
for i in range(n):
    lista = list(map(int, input().split()))
    listas.append(lista)

exclusivos = set(listas[0])
for lista in listas[1:]:
    exclusivos -= set(lista)

resultado = sorted(exclusivos)
print(resultado)

"solucao do professor"


"""
n = int(input())

resp = set(input().spilt())
for i in range(1,n):
    s = set(input().split())
    resp = resp.difference(s)
ret = list(resp)    
for i in range(let(ret)):
   ret[i] = int(ret[i])
   
ret.sort()
print(ret)



Este código Python solicita ao usuário um número inteiro `n` como entrada e depois solicita `n` listas de números separados por espaços. Ele então encontra os números exclusivos (ou seja, que aparecem apenas em uma das listas) e os imprime em ordem crescente.
 Vamos explicar cada parte do código detalhadamente:

1. `n = int(input())`: Aqui, o programa solicita ao usuário um número inteiro `n` como entrada. Este número representa quantas listas de números serão inseridas pelo usuário.

2. `listas = []`: É inicializada uma lista vazia chamada `listas` que será usada para armazenar as listas de números fornecidas pelo usuário.

3. `for i in range(n):`: Este loop é executado `n` vezes para solicitar `n` listas ao usuário.

4. `lista = list(map(int, input().split()))`: Dentro do loop, o programa solicita uma lista de números ao usuário, 
os separa usando `split()` e então mapeia a função `int` para converter cada elemento em um número inteiro. A
 lista resultante é armazenada na variável `lista`.

5. `listas.append(lista)`: A lista `lista` é adicionada à lista de listas `listas`.

6. `exclusivos = set(listas[0])`: Inicializa um conjunto (`set`) chamado `exclusivos` com os elementos da primeira lista (índice 0)
 para começar a encontrar os números exclusivos.

7. `for lista in listas[1:]:`: Este loop itera sobre cada lista a partir da segunda lista até a última na lista de `listas`.

8. `exclusivos -= set(lista)`: A operação `-=` é usada para subtrair do conjunto `exclusivos` o conjunto de elementos presentes na lista atual. Isso significa que estamos removendo os elementos que não são exclusivos em relação às outras listas.

9. `resultado = sorted(exclusivos)`: Depois de encontrar todos os números exclusivos, o conjunto `exclusivos` é convertido em uma lista e ordenado em ordem crescente usando a função `sorted()`. O resultado ordenado é armazenado na variável `resultado`.

10. `print(resultado)`: Por fim, o programa imprime a lista de números exclusivos em ordem crescente.

Resumindo, o código permite que o usuário insira várias listas de números e encontra os números que aparecem exclusivamente em uma das listas. Esses números exclusivos são então ordenados e impressos."""