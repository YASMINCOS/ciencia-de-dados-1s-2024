# Lendo o valor
valor = int(input())

# Lista de valores de cédulas
cedulas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

# Iterando sobre a lista de cédulas
for cedula in cedulas:
    # Calculando a quantidade de cédulas necessárias
    qtd_cedulas = valor // cedula
    # Atualizando o valor para o próximo cálculo
    valor =  valor % cedula 
    # Imprimindo a quantidade de cédulas necessárias
    print(f'{qtd_cedulas} nota(s) de R$ {cedula},00')


#exemplo:576
    #primeira vez entrando no for ele vai ler primeiro elemento da lista que e 100, ou seja, ele vai pegar o inteiro da 
    #divisao de valor(576) pela cedula, que no caso e 100, nesse caso ele da 5 (qtd_celulas)
    #apos isso, ele atualiza o valor, ou seja, o valor passa ser o RESTO do valor(576) pela cedula de 100, que vai ser 76
    #e o processo se repete



#1. `qtd_cedulas = valor // cedula`: Esta linha calcula a quantidade de cédulas necessárias para a cédula atual. 

 #  - O operador `//` é usado para divisão inteira. Ele divide o valor total pelo valor da cédula e retorna a parte inteira do resultado, ou seja, quantas vezes o valor total cabe no valor da cédula.

#2. `valor %= cedula`: Esta linha atualiza o valor total para o próximo cálculo.

 #  - O operador `%=` é uma abreviação para `valor = valor % cedula`, onde `%` é o operador de módulo. Ele calcula o resto da divisão entre `valor` e `cedula`, e então atualiza `valor` com esse resto. Isso garante que, na próxima iteração do loop, estaremos considerando apenas o valor restante após retirar as cédulas do valor total.

#Essas duas linhas são usadas em conjunto para calcular a quantidade de cédulas necessárias e atualizar o valor total para o próximo cálculo na iteração seguinte do loop. Isso permite calcular a quantidade correta de cédulas para cada valor de cédula na lista.
