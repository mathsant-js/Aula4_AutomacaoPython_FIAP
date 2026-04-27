cp =  0

while cp < 10:
    cp += 1

    if cp == 3 or cp == 5:
        # Modificador de fluxo, pula para a próxima iteração
        continue

    if cp == 7:
        # Modificador de fluxo, encerra o laço de repetição e continua o programa
        break

    print(f"Produto {cp}")
    

print()

i = 4

while i > 0:
    print(i)
    i -= 1