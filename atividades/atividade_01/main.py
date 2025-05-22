"""
Crie um programa que receba do usuário dois números reais, e uma das 4 operações da matemática informadas pelo usuário, e faça o cálculo correspondente.
"""

# NOTE - O programa só se encerrará caso o usuário informe isso no programa.

while True:

    x = int(input("Coloque o número inteiro x: "))
    y = int(input("Coloque o número inteiro y: "))

    # menu
    print(f"{'-'*20} CALCULADORA PYTHON{'-'*20}")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")

    menu = input("Insira a opção desejada: ").strip()

    match menu:
        case "1":
            print(f"A soma dos números é: {x+y}")
        case "2":
            print(f"A subratração dos números é: {x-y}")
        case "3":
            print(f"A multiplicação dos números é: {x*y}")
        case "4":
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