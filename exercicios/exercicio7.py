numero = int(input("Digite um número...\n"))
soma = 0

while numero < 0:
    numero = int(input("Digite o número novamente...\n"))

for count in range(1, numero + 1):
    soma += count

print(f"Soma dos números entre 0 e {numero}: {soma}")