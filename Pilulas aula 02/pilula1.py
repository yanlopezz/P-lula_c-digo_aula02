import math
#leituras
assinantes = int(input("Digite a quantidade de assinantes: "))
mensalidade = float(input("Digite o valor da mensalidade: "))
taxa = float(input("Digite a taxa de crescimento estimada mensal %: "))
meses = int(input("Digite a quantidade de meses da projeção: "))
#processamento
assinantes_Finais = assinantes * math.pow((1 + taxa),meses)
receita_Final = assinantes_Finais * mensalidade
#saída
print(f'Assinantes estimados: {assinantes_Finais:.0f}')
print(f'Receita final : R$ {receita_Final:.2f}')

