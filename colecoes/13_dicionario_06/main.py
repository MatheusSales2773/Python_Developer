# tupla
chaves = ('Nome', 'Idade', 'E-mail', 'Profissão')
pessoas = [
    {
        chaves[0]: "Alex Machado",
        chaves[1]: 40,
        chaves[2]: "alex@gmail.com",
        chaves[3]: "CEO"
    },
    {
        chaves[0]: "Matheus",
        chaves[1]: 19,
        chaves[2]: "matheus@gmail.com",
        chaves[3]: "Assistente Administrativo"
    }
]

# inserindo novo dicionario
pessoa = {}

# inserindo dados no novo dicionario

try:
    for chave in chaves:
        if chave == "Idade":
            pessoa[chave] = int(input("Informe a Idade: "))
        else:
            pessoa[chave] = input(f"Informe {chave}: ")
        
    pessoas.append(pessoa)
        
    print(f"{pessoa.get(chave[0])}")
except Exception as e:
    print(f"Não foi possível cadastrar nova pessoa. {e}.")
finally:
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave}: {pessoa.get(chave)},")
        print(f"\n{'-'*40}\n")