# TODO - atividade
'''
Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista
- Exibir a lista de nomes
- Pesquisar por um nome na lista
- Sair do programa
'''

nomes = []

while True:
    print('-'*20, 'Lista de nomes', '-'*20)
        # menu
    print("1 - Inserir um nome em uma lista")
    print("2 - Exibir a lista de nomes")
    print("3 - Pesquisar por um nome na lista")
    print("4 - Sair do programa")

    # O usuário escolhe
    try:
        opcoes = int(input("Escolha a opção(1 a 4): "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    match opcoes:
        case 1:
            while True:
                nome = input("Informe o para adicionar nome: ").capitalize().strip()
                nomes.append(nome)

                print(f"{nome} inserido com sucesso ")
                confirmar = input("Deseja inserir outro nome? (s/n) ").lower().strip()

                if confirmar != 's':
                    break

        case 2:         
            print('-'*20, 'Lista de nomes2', '-'*20)
            nomes.sort()
            for nome in nomes:
                print(nome)
    
        case 3:
            pesquisa = input("Informe o nome a ser pesquisado: ").title().strip() 

            if pesquisa in nomes:
                print(f"{pesquisa} encontrado!")
            else:
                print(f"{pesquisa} não encontrado")

        case 4:
            print("Opção Escolhida. Encerrando o programa.")
            break

        case _:
            print("Opção Inválida. Encerrando o programa.")
            break