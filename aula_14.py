def calcular_comissao(valor_imovel, percentual):
    comissao = valor_imovel * percentual
    return comissao


resultado = calcular_comissao(5000000, 0.05)

print(f"Comissão: R$ {resultado:.2f}")

valor_liquido = 5000000 - resultado

print(f"Valor após comissão: R$ {valor_liquido:.2f}")

resultado_2 = calcular_comissao(3000000, 0.04)

print(f"Comissão de 4%: R$ {resultado_2:.2f}")
