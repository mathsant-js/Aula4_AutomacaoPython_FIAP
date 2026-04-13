numero = int(input("Digite um número...\n"))
divisores = ""

for count in range(2, numero + 1):
    if count % 2 == 0:
        divisores += str(count) + " / "

print(f"Divisores positivos de {numero}: {divisores}")