print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Escolha uma operação: "))

if operacao == 1:
 numero1 = int(input("Digite o primeiro número: "))
 numero2 = int(input("Digite o segundo número: "))

 resultado = numero1 + numero2
 print("Resultado:", resultado)
elif operacao == 2: 
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: ")) 

    resultado = numero1 - numero2

    print("Resultado:", resultado)
    print("Você escolheu Subtração")
elif operacao == 3:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado = numero1 * numero2

    print("Resultado:", resultado)
    print("Você escolheu Multiplicação")
elif operacao == 4:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
        print("Você escolheu Divisão")


    
   
