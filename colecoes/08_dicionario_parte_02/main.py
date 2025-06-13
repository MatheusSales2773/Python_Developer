# dicionario 

pessoa = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'cpf': "666.666.666-66"
}

# exibe os dados do dicionario
print(f"Nome: {pessoa['nome']}")
print(f"E-mail: {pessoa.get('email')}")

# exibe dados inexistentes
print(f"Idade: {pessoa.get('Idade')}")

# Inserindo a idade da pessoa
try:
    pessoa['idade'] = int(input("Informe a idade: "))
    print(f"Nome: {pessoa.get('nome')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"Idade: {pessoa.get('idade')}")
except Exception as e:
    print(f"Não foi possível inseriro o novo valor. {e}")
    

# outra opção

'''
try:
    pessoa['idade'] = int(input("Informe a idade: "))
except Exception as e:
    print(f"Não foi possível inseriro o novo valor. {e}")
finally:
    print(f"Nome: {pessoa.get('nome')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"Idade: {pessoa.get('idade')}")
'''
    