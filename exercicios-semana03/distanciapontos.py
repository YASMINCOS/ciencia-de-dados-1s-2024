import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('{:.4f}'.format(distancia))


#O uso de map(float, input().split()) permite ler os valores de entrada como uma única linha e convertê-los diretamente em valores float. Aqui está como funciona:

#input() é usado para ler uma linha de entrada do usuário.
#.split() divide a linha de entrada em substrings com base nos espaços em branco (por padrão).
#map(float, ...) aplica a função float a cada substring resultante da divisão.
#Finalmente, os valores convertidos são atribuídos às variáveis x1, y1, x2 e y2 em uma única linha, usando a atribuição múltipla.


#
#x1, y1 = map(float, input().split())
#x2, y2 = map(float, input().split())

#1. `input()`: Esta função lê uma linha de entrada do usuário.
#2. `.split()`: Divide a linha de entrada em substrings usando espaços em branco como delimitador padrão. Por exemplo, se a entrada for `"1.0 7.0"`, o método `.split()` criará uma lista `["1.0", "7.0"]`.
#3. `map(float, ...)`: Aplica a função `float()` a cada elemento da lista resultante da operação `.split()`. Isso transforma cada string em um número de ponto flutuante. Por exemplo, `map(float, ["1.0", "7.0"])` produz uma lista de floats `[1.0, 7.0]`.
#4. `x1, y1 = ...`: Usa a atribuição múltipla para atribuir os dois elementos da lista resultante a `x1` e `y1` separadamente. O mesmo ocorre para `x2` e `y2`.

#Então, em resumo, a linha `x1, y1 = map(float, input().split())` lê uma linha de entrada, divide-a em substrings, converte cada substring em um número de ponto flutuante e atribui esses valores às variáveis `x1` e `y1`, respectivamente. O mesmo acontece para `x2` e `y2` na linha subsequente.