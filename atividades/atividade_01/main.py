"""
Crie um programa que receba do usuário dois números reais, e uma das 4 operações da matemática informadas pelo usuário, e faça o cálculo correspondente.
"""

# NOTE - O programa só se encerrará caso o usuário informe isso no programa.

while True:
    
    # menu
    print(f"{'-'*20} CALCULADORA PYTHON{'-'*20}")
    print("0 - sair do programa")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")

    menu = input("Insira a opção desejada: ").strip()

    match menu:
        case "0":
            print("Programa encerrado.")
            break
        case "1":
            x = int(input("Coloque o número inteiro x: "))
            y = int(input("Coloque o número inteiro y: "))
            print(f"A soma dos números é: {x+y}")

        case "2":
            x = int(input("Coloque o número inteiro x: "))
            y = int(input("Coloque o número inteiro y: "))            
            print(f"A subratração dos números é: {x-y}")

        case "3":
            x = int(input("Coloque o número inteiro x: "))
            y = int(input("Coloque o número inteiro y: "))
            print(f"A multiplicação dos números é: {x*y}")

        case "4":
            x = int(input("Coloque o número inteiro x: "))
            y = int(input("Coloque o número inteiro y: "))
            print(f"A divisão dos números é: {x/y}")

        case _:
            print("Opção inválida")

    repetir= input("Deseja verificar de novo?  (s/n) ").lower().strip()
    match repetir:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção Inválida.")
            break
    break
