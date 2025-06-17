import os

usuario = {
    'Nome': "Fulano de Tal",
    'Idade': 19,
    'Email': "exemplo@email.com",
    'Telefone': "(61)9999-9000",
    'Profissao': "Programador"
}

print("-"*24, "Alteração de Chaves", "-"*24)

print(f"Nome: {usuario.get('Nome')}")
print(f"Idade: {usuario.get('Idade')}")
print(f"Email: {usuario.get('Email')}")
print(f"Telefone: {usuario.get('Telefone')}")
print(f"Profissão: {usuario.get('Profissao')}")

print('-'*35)
try:
    chave = input("Informe o nome da chave que deseja alterar: ").title().strip()
    print('-'*35)
    alteracao = input(f"Informe a Alteração de {chave}: ")

    if chave in usuario:
        os.system("cls")
        usuario[chave] = alteracao
        print("Chave alterada com Sucesso!")
    else:
        os.system("cls")
        print(f"A chave {chave} não foi encontrada!")


except Exception as e:
    print(f"Error: {e}")

finally:
    print(f"Nome: {usuario.get('Nome')}")
    print(f"Idade: {usuario.get('Idade')}")
    print(f"Email: {usuario.get('Email')}")
    print(f"Telefone: {usuario.get('Telefone')}")
    print(f"Profissão: {usuario.get('Profissao')}")
