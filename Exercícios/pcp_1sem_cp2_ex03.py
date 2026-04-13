cp1 = float(input("Digite a nota da cp1: "))
cp2 = float(input("Digite a nota da cp2: "))
cp3 = float(input("Digite a nota da cp3: "))
sp1 = float(input("Digite a nota da sp1: "))
sp2 = float(input("Digite a nota da sp2: "))
gs = float(input("Digite a nota da gs: "))

# descobrir menor cp
if cp1 <= cp2 and cp1<= cp3:
    menor = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menor = cp2
else:
    menor = cp3

# soma das cps
soma_cp = cp1 + cp2 + cp3 - menor

# média das cps + sprints
media_parcial = (soma_cp + sp1 + sp2) / 4


# média final
media = (media_parcial * 0.4) + (gs * 0.6)

#média com peso
media_peso = media * 0.4

print(f"Média do semestre:", round(media, 1))
print(f"Média com peso:", round(media_peso, 1))