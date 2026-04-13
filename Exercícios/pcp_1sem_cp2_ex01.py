estado = int(input('Digite o código de estado (1 a 5): '))
peso = int(input('Digite o peso em toneladas da carga do caminhão: '))
codigo = int(input('Digite o código da carga do caminhão (10 a 40): '))

peso *= 1000
precokg = 0
imposto = 0

if codigo >= 10 and codigo <= 20:
    precokg = 100
elif codigo > 20 and codigo <= 30:
    precokg = 250
elif codigo > 30 and codigo <= 40:
    precokg = 340

preco = precokg * peso

if estado == 1:
    imposto = 35
elif estado == 2:
    imposto = 25
elif estado == 3:
    imposto = 15
elif estado == 4:
    imposto = 5
elif estado == 5:
    imposto = 0

valor_imposto = preco * imposto/100

print(f'Peso em KG: {peso}')
print(f'Preço da carga: {preco}')
print(f'Valor do imposto: {valor_imposto}')
print(f'Valor transportado pelo caminhão {preco + valor_imposto}')