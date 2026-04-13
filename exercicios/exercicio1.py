while True:
    print("Olá Mundo!")
    resposta = input("Deseja exibir a mensagem novamente? (s/n)\n").lower

    if resposta != "s":
        break

print("Programa encerrado!")