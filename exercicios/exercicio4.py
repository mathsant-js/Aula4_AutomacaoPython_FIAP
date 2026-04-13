somaNumeros = 0
qtdnumero = 1

for count in range(5):
    somaNumeros += float(input(f"Digite o {qtdnumero}º número...\n"))
    qtdnumero += 1

print(f"Soma dos números: {somaNumeros}")