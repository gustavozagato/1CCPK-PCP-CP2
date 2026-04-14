def menor_cp(cp1, cp2, cp3):
    menor = 0
    if cp1 <= cp2 and cp1<= cp3:
        menor = cp1
    elif cp2 <= cp1 and cp2 <= cp3:
        menor = cp2
    else:
        menor = cp3
    return menor

def menorque10(cp1,cp2,cp3,sp1,sp2,gs):
    pode_calcular = False
    if cp1 > 10 or cp2 > 10 or cp3 > 10 or sp1 > 10 or sp2 > 10 or gs > 10:
        print('Nota inválida.')
    else:
        pode_calcular = True
    return pode_calcular

cp1 = float(input("Digite a nota da cp1: "))
cp2 = float(input("Digite a nota da cp2: "))
cp3 = float(input("Digite a nota da cp3: "))
sp1 = float(input("Digite a nota da sp1: "))
sp2 = float(input("Digite a nota da sp2: "))
gs = float(input("Digite a nota da gs: "))

if menorque10(cp1,cp2,cp3,sp1,sp2,gs):
    # soma das cps
    soma_cp = cp1 + cp2 + cp3 - menor_cp(cp1, cp2, cp3)

    # média das cps + sprints
    media_parcial = (soma_cp + sp1 + sp2) / 4

    # média final
    media = (media_parcial * 0.4) + (gs * 0.6)

    #média com peso
    media_peso = media * 0.4

    print(f"Média do semestre: {media:.1f}")
    print(f"Média com peso: {media_peso:.1f}")