import statistics as st
lote1 = float(input('Produção do lote 1: '))
lote2 = float(input('Produção do lote 2: '))
lote3 = float(input('Produção do lote 3: '))
media = st.mean( (lote1, lote2, lote3) )
desvio = st.stdev( (lote1,lote2, lote3) )
print(f'Média {media:.2f}')
print(f'Desvio padrão {desvio:.2f}')