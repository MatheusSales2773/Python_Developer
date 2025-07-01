from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(
        nome="",
        cpf="",
        profissao="",
        email="",
        telefone="",
        endereco=""
    )

    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereco=""
    )

    print(f"{"-"*20}Informe os dados do usuário{"-"*20}\n")

    usuario.nome = input("Informe o nome do usuário: ")
    usuario.cpf = input("Informe o cpf do usuário: ")
    usuario.email = input("Informe o email do usuário: ")
    usuario.telefone = input("Informe o telefone do usuário: ")
    usuario.profissao = input("Informe o profissao do usuário: ")
    usuario.endereco = input("Informe o endereço do usuário: ")

    # limpar
    limpar()

    print(f"{"-"*20}Informe os dados da empresa{"-"*20}\n")
    
    empresa.nome_social = input("Informe o nome social da empresa: ")
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ")
    empresa.cnpj = input("Informe o cnpj da empresa: ")
    empresa.email = input("Informe o email da empresa: ")
    empresa.telefone = input("Informe o telefone da empresa: ")
    empresa.endereco = input("Informe o endereço da empresa: ")

    limpar()

    # saida de dados
    print(usuario)
    print()
    print(empresa)
