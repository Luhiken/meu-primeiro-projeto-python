cliente = {
    "nome": "Ana",
    "idade": 45,
    "cidade": "São Paulo",
    "interesse": "Apartamento"
}

print(cliente)

print(cliente["nome"])
print(cliente["cidade"])
print(cliente["interesse"])

cliente["interesse"] = "Apartamento de alto padrão"

print(cliente)
print(cliente["interesse"])
cliente["interesse"] = "Apartamento de alto padrão"

cliente["investimento"] = 5000000

print(cliente)
print(cliente["investimento"])

del cliente["idade"]

print(cliente)
imovel = {
    "empreendimento": "San Paolo",
    "bairro": "Alto de Pinheiros",
    "metragem": 277,
    "valor": 15000000
}

print(imovel)
print(imovel["empreendimento"])
print(imovel["metragem"])
print(imovel["valor"])