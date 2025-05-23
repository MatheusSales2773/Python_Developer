"""
Crie um programa que receba o nome do usuário e informe o menu abaixo:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Frango Assado - 18 anos
O usuário deverá escolher a sala do filme que deseja assistir, e o programa deverá:
- Liberar a entrada do usuário e encerrar, caso o usuário tenha a idade mínima, ou maior.
- Bloquear a entrada do usuário e pedir para o mesmo escolher outro filme, caso não tenha a idade mínima.
"""

# O usuário informa os números
nome = input("Coloque seu nome: ")
idade = int(input("Qual sua idade: "))

while True:

    # menu
    print("Sala 1 - A Roda Quadrada - Livre")
    print("Sala 2 - A Volta dos Que Não Foram - 12 anos")
    print("Sala 3 - Poeira em Alto Mar - 14 anos")
    print("Sala 4 - As tranças do Rei Careca - 16 anos")
    print("Sala 5 - A Vingança do Frango Assado - 18 anos")

    # O usuário escolhe a operação
    salas = input("Escolha o número da Sala: ").strip()

    match salas:
        case "1":
            print(f"{nome} decidiu assistir A Roda Quadrada - Livre")
            choice = "A Roda Quadrada"

        case "2": 
            print(f"{nome} decidiu assistir A Volta dos Que Não Foram - 12 anos" if idade >= 12 else "Idade não permitida. Escolha outro filme")
            choice = "A Volta dos Que Não Foram"

        case "3":
            print(f"{nome} decidiu assistir Poeira em Alto Mar - 14 anos" if idade >= 14 else "Idade não permitida. Escolha outro filme")
            choice = "Poeira em Alto Mar"

        case "4":
            print(f"{nome} As tranças do Rei Careca - 16 anos" if idade >= 16 else "Idade não permitida. Escolha outro filme")
            choice = "As tranças do Rei Careca"

        case "5":
            print(f"{nome} decidiu assistir A Vingança do Frango Assado - 18 anos" if idade >= 18 else "Idade não permitida. Escolha outro filme")
            choice = "A Vingança do Frango Assado"
        
        case _:
            print("Número da sala incorreto, porfavor escolha um número de 1 a 5")
    
    # Pergunta se o usuário deseja escolher outro filme
    confirmação = input("Deseja escolher outro filme? (s/n): ").strip().lower()
    if confirmação in ["s", "sim", "ss"]:
        print("Escolha outro filme, porfavor")
    elif confirmação in ["n", "não", "nao"]:
        print(f"Obrigado pela preferência {nome} e por escolher o {choice}, bom filme!!!")
        break
    else:        
        print("Opção inválida. Encerrando o programa.")
        break
