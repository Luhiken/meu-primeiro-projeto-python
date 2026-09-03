def saudacao():
    print("Olá! Seja bem-vindo ao meu sistema de leads!")

saudacao()

def apresentar_cliente(nome):
    print("Cliente:", nome)

apresentar_cliente("Luciana")
apresentar_cliente("João")
apresentar_cliente("Marcelo")
apresentar_cliente("Liana")

def calcular_comissao(valor):
    comissao = valor * 0.05
    return comissao
print(calcular_comissao(5000000))

def classificar_lead(valor):
    if valor >= 3000000:
        return "Alto padrão"
    else:
        return "Médio padrão"

print(classificar_lead(2500000))

def classificar_lead(valor):
    if valor >= 3000000:
        return "Alto padrão"
    else:
        return "Médio padrão"
print(classificar_lead(5000000))
