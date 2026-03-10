import statistics
lote1 = float(input("Produção lote1: "))
lote2 = float(input("Produção lote2: "))
lote3 = float(input("Produção lote3: "))
media = statistics.mean((lote1,lote2,lote3))
desvio = statistics.stdev((lote1, lote2,lote3))
print(f'media: {media:.2f}')
print(f'desvio padrão: {desvio:.2f}')