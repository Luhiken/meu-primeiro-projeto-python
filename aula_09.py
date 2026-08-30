print("Iniciando apresentação...")

for numero in range(5, 0, -1):
    print(numero)

print("Começou!")

quantidade = int(input("Até qual número você quer contar? "))

for numero in range(1, quantidade + 1):
    print(numero)

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

for numero in range(inicio, fim + 1):
    print(numero)

inicio = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))
passo = int(input("Digite o passo: "))

for numero in range(inicio, final + 1, passo):
    print(numero)