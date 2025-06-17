import os

usuario = {
    'Nome': "Fulano",
    'Idade': 18,
    'Email': "exemplo@exemplo.com",
    'Profissao': "Programador"
}

# deletar chave

try:
    print(f"Nome: {usuario.get('Nome')}")
    print(f"Idade: {usuario.get('Idade')}")
    print(f"Email: {usuario.get('Email')}")
    print(f"Profissão: {usuario.get('Profissao')}")
    print('-'*24)
    chave = input("Informe a Chave que deseja Deletar: ").title().strip()

    if chave in usuario:
        os.system("cls")
        print(f"{chave} deletada com sucesso!")
        del(usuario[chave])
    else:
        os.system("cls")
        print(f"{chave} Não existe na Lista!")
 
except Exception as e:
    print("Error: {e}")

finally:
    print("")
    print('-'*24)
    print("")
    for chave in usuario:
        print(f"{chave}: {usuario.get(chave)}")
    print("")