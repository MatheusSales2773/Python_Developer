from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":

    usuario = PessoaFisica(nome="", cpf="", profissao="", email="", telefone="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="")

    print(f"{'-'*20}Dados do Usuário{'-'*20}\n")
          
    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu cpf: ").strip()
    usuario.profissao = input("Informe seu profissao: ").strip()
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.endereco = input("Informe seu endereço: ").strip()
    usuario.telefone = input("Informe seu telefone: ").strip()

    limpar()

    print(f"{'-'*20}Dados da Empresa{'-'*20}\n")

    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantasia: ").title().strip()
    empresa.cnpj = input("Informe o cnpj da empresa: ").strip()
    empresa.email = input("Informe o email da empresa: ").lower().strip()
    empresa.endereco = input("Informe o endereço da empresa: ").title().strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    print(f"{'-'*20}Dados do Usuário{'-'*20}\n")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Profissão: {usuario.profissao}")
    print(f"Email: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

    print(f"{'-'*20}Dados da Empresa{'-'*20}\n")
    print(f"Razão social: {empresa.razao_social}")
    print(f"Nome Fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Email: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")