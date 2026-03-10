import random
cotacao = float(input('Cotação atual do dolar:'))
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
print(f'Variação simulada; {variacao:.3%}')
print(f'Nova cotação: {nova_cotacao:.2f}')
#random.uniform é variação aleatória do número detro dos ()

