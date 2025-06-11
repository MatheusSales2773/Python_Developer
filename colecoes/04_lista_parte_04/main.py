cidades = [
    "Cuiaba",
    "Florianopolis",
    "Natal",
    "São Paulo",
    "Muriaé",
    "Brasília",
    "Fortaleza",
    "Rio de Janeiro",
    "Jeri",
    "Xique-Xique",
    "Goiânia",
    "Belo Horizonte",
    "Rio Branco",
    "Manaus",
    "Xique-Xique",
    "Goiânia",
    "Belo Horizonte",
    "Rio Branco",
]

# usuário faz a pesquisa
pesquisa = input("Informe o nome da cidade a ser pesquisada: ").title().strip() # .title() transforma a primeira letra de cada palavra em maiúscula, e o restante em minúsculas.
quantidade = cidades.count(pesquisa)

'''if pesquisa in cidades:
    print(f"{pesquisa} encontrado!")
else:
    print(f"{pesquisa} não encontrado")'''
print(f"{pesquisa} foi encontrado {quantidade} vezes na lista")