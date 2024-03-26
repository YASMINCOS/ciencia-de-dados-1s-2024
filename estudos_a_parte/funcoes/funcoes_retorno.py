


def calculo_conta(consumo, taxa_servico, desconto):
    if taxa_servico == 0 and desconto == 0:
        return consumo
    
    servico = consumo * taxa_servico
    desconto = consumo * desconto 

    valor = consumo + servico 
    valor = valor - desconto
    return valor

valor = calculo_conta(100, 0.15, 0.1)
print("O valor é:" , valor)
"""
consumo = 100
servico = consumo * taxa_servico
desconto = consumo * desconto 

valor = consumo + servico 
valor = valor - desconto 

"""