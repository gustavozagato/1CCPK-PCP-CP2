def pode_aprovar(idade, renda, valor):
    aprovado = False
    if idade >= 18:
        if renda*20 > valor > 0:
            print('Aprovado!')
            aprovado = True
        else:
            print('Não aprovado: valor não correspondente ao permitido')
    else:
        print('Não aprovado: menor de idade.')
    return aprovado

def definir_taxa(parcelas):
    taxa = 0.0
    if parcelas <= 6 and parcelas > 0:
        taxa = 0.05
    elif parcelas > 6 and parcelas <= 12:
        taxa = 0.08
    elif parcelas > 12 and parcelas <= 24:
        taxa = 0.10
    else:
        print('Número de parcelas inválido')
    return taxa

def calcular_parcela(valor, taxa, parcelas):
    pmt = valor * taxa * (1+taxa)**parcelas / ((1+taxa)**parcelas-1)
    return pmt

def calcular_total(parcela,parcelas):
    total_pago = parcela * parcelas
    return total_pago

def calcular_juros(total,valor):
    juros = total - valor
    return juros

nome_cliente = input('Digite seu nome: ')
idade_cliente = int(input('Digite sua idade: '))
renda_cliente = float(input('Digite sua renda mensal: '))
valor_desejado =  float(input('Digite o valor desejado: '))
parcela = int(input('Digite o número de parcelas: '))

if pode_aprovar(idade_cliente,renda_cliente,valor_desejado):
    taxa_juros = float(definir_taxa(parcela))
    if 0 < parcela <= 24:
        pmt = float(calcular_parcela(valor_desejado,taxa_juros,parcela))
        total_pago = float(calcular_total(parcela,pmt))
        juros = float(calcular_juros(total_pago,valor_desejado))
        print(f'Nome do cliente: {nome_cliente}')
        print(f'Valor financiado: {valor_desejado}')
        print(f'Taxa de juros: {taxa_juros}')
        print(f'Número de parcelas: {parcela}')
        print(f'Valor total pago: {total_pago:.2f}')
        print(f'Total de juros pago: {juros:.2f}')