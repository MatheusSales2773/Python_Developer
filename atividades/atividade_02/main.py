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
# TODO

nome = input("Coloque seu nome: ")
idade = int(input("Qual sua idade: "))

# menu
print("Sala 1 - A Roda Quadrada - Livre")
print("Sala 2 - A Volta dos Que Não Foram - 12 anos")
print("Sala 3 - Poeira em Alto Mar - 14 anos")
print("Sala 4 - As tranças do Rei Careca - 16 anos")
print("Sala 5 - A Vingança do Frango Assado - 18 anos")

salas = input("Escolha o número da Sala: ").strip()

match salas:
    case "1":
        print("")
    case _:
        print("Número Incorreto")
        break