import math


""""RECEBE A ENTRADA COM UMA LISTA DE NUMETOS"""
entrada = input().split()


""""PEGA OS VALORES SEPARADAMENTE"""
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])


""""REALIZA A CONTA"""
delta = B ** 2 - 4 * A * C


""""VERIFICA SE DELTA E MENOR QUE 0 O A E IGUAL A 0"""
if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")