"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Inserir dados 
- Exibir lista de usuários
- Alterar dados de um usuário já cadastrado
- Excluir usuário da lista
- Sair do programa
Os dados a serem cadastrados serão as seguintes:
- Nome
- Data de Nascimento
- E-mail
- CPF 
- Telefone
- Profissão
- Gênero
# NOTE - a lista deve começar vazia
"""
import os
lista = []

while True:
    print("1 - Inserir dados")
    print("2 - Exibir lista de usuários")
    print("3 - Alterar dados de um usuário já cadastrado")
    print("4 - Excluir usuário da lista")
    print("5 - Sair do programa")

    try:
        opcoes = int(input("Escolha a opção(1 a 5): "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue   
    os.system("cls")

    match opcoes:
        case 1: 
            print("\n" + "-"*20 + " Inserir novo Usuário " + "-"*20)
            usuario = {
                "Nome": input("Nome: ").strip().title(),
                "Data de Nascimento": input("Data de Nascimento (DD/MM/AAAA): ").strip(),
                "E-mail": input("E-mail: ").strip(),
                "CPF": input("CPF: ").strip(),
                "Telefone": input("Telefone: ").strip(),
                "Profissão": input("Profissão: ").strip(),
                "Gênero": input("Gênero: ").strip()
            }
            os.system("cls")
            lista.append(usuario)
            continue

        case 2:
            print("\n" + "-"*20 + " Exibir lista de usuários " + "-"*20)
            if not lista:
                print("Não há lista")
            else:
                for pessoa in lista: 
                    for chave in pessoa:
                        print(f"{chave.capitalize()}: {pessoa.get(chave)}")
                    print(f"\n{'-'*40}\n")
            print()
            continue

        case 3:
            if not lista:
                print("Não há usuários cadastrados para alterar.")
                continue

            print("Buscar usuário por:")
            print("1 - CPF\n2 - Nome\n3 - E-mail\n4 - Telefone")
            opcao = input("Opção: ").strip()
            chaves = {"1": "CPF", "2": "Nome", "3": "E-mail", "4": "Telefone"}

            if opcao not in chaves:
                print("Opção inválida.")
                continue

            chave_busca = chaves[opcao]
            valor_busca = input(f"Digite o {chave_busca} do usuário: ").strip().lower()

            encontrados = [p for p in lista if p.get(chave_busca, "").lower() == valor_busca]

            if not encontrados:
                print("Usuário não encontrado.")
                continue

            # Se mais de um encontrado, lista todos com índice
            if len(encontrados) > 1:
                print(f"Foram encontrados {len(encontrados)} usuários:")
                for idx, pessoa in enumerate(encontrados):
                    print(f"{idx} - {pessoa['Nome']} | CPF: {pessoa['CPF']} | Email: {pessoa['E-mail']}")
                try:
                    selecionado = int(input("Escolha o número do usuário que deseja alterar: "))
                    usuario = encontrados[selecionado]
                except (ValueError, IndexError):
                    print("Seleção inválida.")
                    continue
            else:
                usuario = encontrados[0]

            print(f"Usuário selecionado: {usuario['Nome']}")
            campo = input("Informe o campo que deseja alterar (ex: Nome, Profissão, Telefone): ").strip().capitalize()

            if campo in usuario:
                novo_valor = input(f"Novo valor para {campo}: ").strip()
                usuario[campo] = novo_valor
                os.system("cls")
                print(f"{campo} alterado com sucesso!\n")
            else:
                print(f"Campo '{campo}' não encontrado.")

        case 4:
            if not lista:
                print("Não há usuários cadastrados.")
                continue

            chave_busca = {"1": "CPF", "2": "Nome", "3": "E-mail", "4": "Telefone"}.get(input(
                "Buscar por:\n1 - CPF\n2 - Nome\n3 - E-mail\n4 - Telefone\nOpção: ").strip())

            if not chave_busca:
                print("Opção inválida.")
                continue

            valor = input(f"Digite o {chave_busca}: ").strip().lower()
            encontrados = [p for p in lista if p.get(chave_busca, "").lower() == valor]

            if not encontrados:
                print("Nenhum usuário encontrado.")
                continue

            print("\nUsuários encontrados:")
            for i, p in enumerate(encontrados, 1):
                print(f"[{i}] Nome: {p['Nome']} | CPF: {p['CPF']} | E-mail: {p['E-mail']}")

            cpf_confirmado = input("\nDigite o CPF do usuário a ser excluído: ").strip()
            for pessoa in lista:
                if pessoa["CPF"] == cpf_confirmado:
                    confirm = input("Confirmar exclusão? (s/n): ").strip().lower()
                    if confirm == "s":
                        lista.remove(pessoa)
                        os.system("cls")
                        print("Usuário excluído com sucesso!\n")
                    else:
                        print("Exclusão cancelada.\n")
                    break
            else:
                print("CPF não encontrado.")


        case 5: 
            print("Encerrando programa...")
            break
