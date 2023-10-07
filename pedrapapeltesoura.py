jogador1 = 0
jogador2 = 0

while jogador1 < 2 and jogador2 < 2:

    opcaojogador1 = input(
        "Jogador 1, digite:\n"
        "1 para pedra\n"
        "2 para papel\n"
        "3 para tesoura\n"
        "s para finalizar partida\n"
        "Digite a opção: ")

    while opcaojogador1 not in "123sS":
        print("Opção inválida")
        opcaojogador1 = input(
            "Jogador 1, digite:\n"
            "1 para pedra\n"
            "2 para papel\n"
            "3 para tesoura\n"
            "s para finalizar partida\n"
            "Digite a opção: ")

    if opcaojogador1 == "s" or opcaojogador1 == "S":
        print("Programa finalizado")
        exit()

    opcaojogador2 = input(
        "Jogador 2, digite:\n"
        "1 para pedra\n"
        "2 para papel\n"
        "3 para tesoura\n"
        "s para finalizar partida\n"
        "Digite a opção: ")

    while opcaojogador2 not in "123sS":
        print("Opção inválida")
        opcaojogador2 = input(
            "Jogador 2, digite:\n"
            "1 para pedra\n"
            "2 para papel\n"
            "3 para tesoura\n"
            "s para finalizar partida\n"
            "Digite a opção: ")

    if opcaojogador1 == opcaojogador2:
        print("A partida terminou em empate.")
    elif (opcaojogador1 == "1" and opcaojogador2 == "3") or \
         (opcaojogador1 == "2" and opcaojogador2 == "1") or \
         (opcaojogador1 == "3" and opcaojogador2 == "2"):
        jogador1 += 1
        print(f"Jogador 1 venceu a rodada {jogador1}.")
    else:
        jogador2 += 1
        print(f"Jogador 2 venceu a rodada {jogador2}.")

if jogador1 > jogador2:
    print("Jogador 1 venceu a melhor de 3!")
else:
    print("Jogador 2 venceu a melhor de 3!")



