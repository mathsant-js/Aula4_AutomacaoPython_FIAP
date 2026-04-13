numero = int(input("Digite um número...\n"))
pares = ""

for count in range(2, numero):
    if count % 2 == 0:
        pares += str(count) + " / "

print(f"Os números pares são: {pares}")