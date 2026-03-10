import math
#leituras
assinantes = int(input('Digite a quantidade de assinantes atuais: '))
mensalidade = float(input('Digite o valor da mensalidade: '))
taxa = float(input('Digite a taxa de crescimento mensal %: '))
meses = int(input('Digite a qtd de meses a projeção: '))
#processamento
assinantes_finais = assinantes * math.pow((1 + taxa / 100), meses)
receita_final = assinantes_finais * mensalidade
#saída
print(f'Assinantes estimados: {assinantes_finais:.0f}')
print(f'Receita estimada: R$ {receita_final:.2f}')