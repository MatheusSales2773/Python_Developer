import classes
import os

if __name__ == "__main__":
    usuario = classes.PessoaFisica("", "", "", "",  "", "",)
    empresa = classes.PessoaJuridica("", "", "", "",  "", "",)

    while True:
        print('-'*24, "Inserir Dados", '-'*24)
        print("[1] Inserir dados de usuário")
        print("[2] Inserir dados de empresa")
        print("[3] Exibir dados")
        print("[4] Sair do programa")
        print('-'*67)
        print("")

        choose = input("Escolha uma opção: ").strip()

        match choose:
            case "1":
                try:
                    usuario.nome = input("Informe seu nome: ").title().strip()
                    usuario.cpf = input("Informe seu cpf: ").strip()
                    usuario.profissao = input("Informe seu profissao: ").strip()
                    usuario.email = input("Informe seu email: ").strip().lower()
                    usuario.endereco = input("Informe seu endereço: ").strip()
                    usuario.telefone = input("Informe seu telefone: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados do usuario {usuario.nome} inseridos com sucesso!")

                except Exception as e:
                    print(f"Não foi possível inserir os dados do usuário. {e}.")
                finally:
                    continue
            case "2":
                try:
                    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
                    empresa.nome_fantasia = input("Informe o nome fantasia: ").title().strip()
                    empresa.cnpj = input("Informe o cnpj da empresa: ").strip()
                    empresa.email = input("Informe o email da empresa: ").lower().strip()
                    empresa.endereco = input("Informe o endereço da empresa: ").title().strip()
                    empresa.telefone = input("Informe o telefone da empresa: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados da empresa {empresa.nome_fantasia} inseridos com sucesso!")
                except Exception as e:
                        print(f"Não foi possível inserir os dados do usuário. {e}.")
                finally:
                    continue
            case "3":
                os.system("cls" if os.name == "nt" else "clear")
                if usuario.nome != "" and empresa.nome_fantasia != "":
                    usuario.exibir_dados()
                    empresa.exibir_dados()
                elif usuario.nome == "" and empresa.nome_fantasia != "":
                    empresa.exibir_dados()
                elif usuario.nome != "" and empresa.nome_fantasia == "":
                    usuario.exibir_dados()

            case "4":
                print("Encerrando programa")
                break
            case _:
                print("Opção inválido.")
                continue