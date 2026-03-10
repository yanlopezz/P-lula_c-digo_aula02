import random
cotação = float(input("Cotação atual do dólar: "))
variação = random.uniform(-0.015, 0.015)
nova_cotação = cotação * (1 + variação)
print(f'Variação simulada: {variação:.3%}')
print (f'Nova cotação: {nova_cotação:.2f}')
