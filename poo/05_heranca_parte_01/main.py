import classes
import os

if __name__ == "__main__":
    # instancia de objetos
    usuario = classes.PessoaFisica("", "", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")

    # atribuição ao objeto do tipo Pessoa Fisica
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}\n")

    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu cpf: ").strip()
    usuario.profissao = input("Informe seu profissao: ").strip()
    usuario.genero = input("Informe seu genero: ").title().strip()
    usuario.email = input("Informe seu email: ").strip()
    usuario.endereco = input("Informe seu endereço: ").strip()
    usuario.telefone = input("Informe seu telefone: ").strip()
    
    # limpar tela
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n")
    # atribuir valores ao objeto do tipo Pessoa Juridica
    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantasia: ").title().strip()
    empresa.cnpj = input("Informe o cnpj da empresa: ").strip()
    empresa.email = input("Informe o email da empresa: ").lower().strip()
    empresa.endereco = input("Informe o endereço da empresa: ").title().strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    # exibe os dados dso usuario e da empresa
    print("Dados do usuário:\n")
    usuario.exibir_dados()
    print("-"*60)
    print("Dados da empresa:\n")
    empresa.exibir_dados()    