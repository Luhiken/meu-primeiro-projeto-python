while True:

    nome = input("Digite o nome do cliente: ")

    if nome == "":
        continue

    if nome == "sair":
        break

    print(f"cliente: {nome}")