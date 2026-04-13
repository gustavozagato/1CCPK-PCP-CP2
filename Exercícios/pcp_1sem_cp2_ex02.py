def triangulo(A, B, C):
    resultado = ''
    if A >= B + C:
        resultado = 'Não forma triângulo'
    elif A == B == C:
        resultado = 'Triângulo equilátero'
    elif A == B or B == C:
        resultado = 'Triângulo isósceles'
    elif A**2 == B**2 + C**2:
        resultado = 'Triângulo retângulo'
    elif A**2 > B**2 + C**2:
        resultado = 'Triângulo obtusângulo'
    elif A**2 < B**2 + C**2:
        resultado = 'Triângulo acutângulo'
    return resultado

lados = []
valor1 = int(input('Digite o primeiro lado: '))
valor2 = int(input('Digite o segundo lado: '))
valor3 = int(input('Digite o terceiro lado: '))
lados.append(valor1)
lados.append(valor2)
lados.append(valor3)
lados.sort(reverse=True)
A = lados[0]
B = lados[1]
C = lados[2]

print(f'O resultado é: {triangulo(A,B,C)}')
