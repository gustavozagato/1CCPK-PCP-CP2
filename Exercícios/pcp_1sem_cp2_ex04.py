nome_funcionario = input("Qual o seu nome?: ")
cargo = int(input("digite 1 se você é Gerente, 2 para Analista, 3 para Assistente e 4 e para Estagiario: "))
salario_base = float(input("Qual o seu salario?: "))
hora_extra_trabalha = int(input("Qual a sua hora trabalhada?: "))
falta_mes = int(input("Quantas vezes vc faltou?: "))
recebeu_bonus = input("Coloque S ou N se voce recebeu bonus?: ") # o usuario deve digitar em minusculo


salario_multiplicado = (salario_base * 1.5 / 100) * hora_extra_trabalha
desconto_falta = (salario_base * 2 / 100) * falta_mes

def qual_o_cargo():
    if cargo == 1:
        return "Gerente"
    elif cargo == 2:
        return "Analista"
    elif cargo == 3:
        return "Assistente"
    elif cargo == 4:
        return "Estagiario"
    else:
        return "Cargo Inválido"

def calcular_bonus():
    if recebeu_bonus == "s":
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

bonus = calcular_bonus()
salario_bruto = salario_base + salario_multiplicado + bonus
total_acrescimos = salario_multiplicado + bonus
total_descontos = desconto_falta
salario_final = salario_bruto - total_descontos

# qual_o_cargo()
# print(f"Salario bruto: {salario_bruto}")
# print(f"Total de acrescimos: {total_acrescimos}")
# print(f"Total de descontos: {total_descontos}")
# print(f"Salario final: {salario_final}")


print(f"Seu nome é {nome_funcionario}, seu cargo é de {qual_o_cargo()}, seu salario bruto é de {salario_bruto}R$, "  
f"Seu total de Acrescimo foi {total_acrescimos}R$, Seu total de desconto foi {total_descontos}R$, O seu salario Final é {salario_final}R$")