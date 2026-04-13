qtdNumeros = 1
numeros = []
higher = 0.0

for count in range(5):
    numero = float(input(f"Digite o {qtdNumeros}º número...\n"))
    qtdNumeros += 1
    numeros.append(numero)
    
    if numeros[count] > higher:
        higher = numeros[count]

print(f"O maior número é {higher}")