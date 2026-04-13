nome_funcionario = input("Qual o seu nome?: ")
cargo = int(input("digite 1 para Gerente, 2 para Analista, 3 para Assistente e 4 para Estagiario "))
salario_base = float(input("Qual o seu salario?: "))
hora_extra_trabalha = int(input("Qual a sua hora trabalhada?: "))
falta_mes = int(input("Quantas vezes vc faltou?: "))
recebeu_bonus = input("Coloque s ou n se voce recebeu bonus: ")

salario_multi = (salario_base * 1.5 /100) * hora_extra_trabalha
desconto_falta = (salario_base * 2 /100) * falta_mes

def qual_o_cargo():
    if cargo ==1:
        print(f"Seu Cargo é de Gerente" )
    elif cargo ==2:
        print("Seu cargo é de Analista")
    elif cargo ==3:
        print("Seu cargo é de Assistente")
    elif cargo ==4:
        print("Você é Estagiario")
    else:
        print("Coloque um numero certo!!")

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

salario_bruto = salario_base + salario_multi + bonus
total_acrescimos = salario_multi + bonus
total_descontos = desconto_falta
salario_final = salario_bruto - total_descontos

qual_o_cargo()

# print(salario_base)
# print(hora_extra_trabalha)
# print(falta_mes)
# print(recebeu_bonus)

print(f"Salario bruto: {salario_bruto}")
print(f"Total de acrescimos: {total_acrescimos}")
print(f"Total de descontos: {total_descontos}")
print(f"Salario final: {salario_final}")

#Incompleto

print(f"nome é {nome_funcionario} seu cargo é {qual_o_cargo()} seu salario bruto é {salario_bruto}, "
      f"Seu total de Acrescimo {total_acrescimos}, Seu total de desconto foi {total_descontos}, O seu salario Final é {salario_final}")

# Fazer depois