tabuada = int(input("Digite a tabuada que deseja: "))

if tabuada >= 1:
    for numero in range(1, 11):
        resultado = tabuada * numero
        print(tabuada, "x", numero, "=", resultado)
else:
    print("Digite um número maior ou igual a 1.")
