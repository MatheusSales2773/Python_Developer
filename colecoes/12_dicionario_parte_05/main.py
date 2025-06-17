pessoas = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com",
        'profissão': "Programador"
    },
    {
        'nome': "Jovem Tranquilão",
        'idade': 120,
        'email': "goatjava@gmail.com",
        'profissão': "Javeiro"
    },
    {
        'nome': "Ciclano",
        'idade': 15,
        'email': "pip@gmail.com",
        'profissão': "Gerente de projetos"
    }
]

# exibir essa lista
for pessoa in pessoas: 
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}.")
    print(f"\n{'-'*40}\n")

# novo dicionario
nova_pessoa = {
        'nome': "Cristiano",
        'idade': 40,
        'email': "cr7@gmail.com",
        'profissão': "O Bode"    
}

# adicionando novo dicionario a lista
pessoas.append(nova_pessoa)

# exibe nova lista de dicionarios
print(f"NOVA LISTA")
for pessoa in pessoas: 
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}.")
    print(f"\n{'-'*40}\n")