# ==========================================
# AULA 10 - BREAK E CONTINUE
# ==========================================


# ------------------------------------------
# EXEMPLO 1 - BREAK
# O break interrompe o loop
# ------------------------------------------

for numero in range(1, 6):
    if numero == 3:
        break

    print(numero)

    # ------------------------------------------
# EXEMPLO 2 - CONTINUE
# O continue pula uma repetição
# ------------------------------------------

for numero in range(1, 10):
    if numero == 5:
        continue

    print(numero)

# ------------------------------------------
# EXEMPLO 3 - BREAK COM LISTA DE CLIENTES
# Para a busca quando encontra Maria
# ------------------------------------------

clientes = ["Ana", "Marcelo", "Maria", "Fernando"]

for cliente in clientes:
    if cliente == "Maria":
        print("Cliente encontrado:", cliente)
        break
# ------------------------------------------
# EXEMPLO 4 - CONTINUE COM LISTA DE CLIENTES
# Pula Maria e continua procurando
# ------------------------------------------

clientes = ["Ana", "Marcelo", "Maria", "Fernando"]

for cliente in clientes:
    if cliente == "Maria":
        continue

    print(cliente)
