clientes = ["Ana", "Ricardo", "Marcelo", "Fernando"]

print(clientes)
print(clientes[0])
print(clientes[2])


empreendimentos = [
    "Expand Pinheiros",
    "145 Vianna",
    "Park Avenue",
    "Ybirá Jurupis",
    "Ybirá Chibarás"
]

print(empreendimentos)

print(empreendimentos[0])
print(empreendimentos[2])


empreendimentos.append("San Paolo")

print(empreendimentos)

print(len(empreendimentos))


for empreendimento in empreendimentos:
    print(empreendimento)


for numero, empreendimento in enumerate(empreendimentos, start=1):
    print(numero, "-", empreendimento)


if "San Paolo" in empreendimentos:
    print("San Paolo está na lista.")


if "Faria Lima" in empreendimentos:
    print("Faria Lima está na lista.")
else:
    print("Faria Lima não está na lista.")


if "145 Vianna" in empreendimentos:
    print("145 Vianna está na lista.")
else:
    print("145 Vianna não está na lista.")


if "Faria Lima" in empreendimentos:
    empreendimentos.remove("Faria Lima")
    print("Faria Lima foi removido da lista.")
else:
    print("Faria Lima não está na lista. Nada foi removido.")