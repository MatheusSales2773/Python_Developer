"""
# TODO - Crie um programa que calcule a equação do 1º grau.
# NOTE - COloque um meno para o usuário decidir se quer calcular a equação ou sair do programa
# NOTE - Coloque no menu a opção de calcular a equação do 2º grau(não precisa desenvolver essa função por enquanto)
# NOTE - Faça usando o conceito de módulo recém-ensinado, usando o comando 'import equacoes' no main.py
"""
import os
import modulo as eq

# algoritmo principal
if __name__ == "__main__":
    while True:
        try:
            # menu
            print("1 - Calcular equação de 1º grau.")
            print("2 - Calcular equação de 2º grau.")
            print("3 - Sair do programa")
            opcao = input("Informe a operação desejada: ").strip()

            os.system("cls" if os.name == "nt" else "clear")

            match opcao:
                case "1":
                    a = float(input("Informe o valor de A: ").replace(",","."))
                    b = float(input("Informe o valor de B: ").replace(",","."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.primeiro_grau(a,b)
                    print(f"{a}x+{b} = 0" if b >= 0 else f"{a}x{b} = 0")
                    print(f"O valor de x é {result}.")
                    continue
                case "2":
                    a = float(input("Informe o valor de A: ").replace(",","."))
                    b = float(input("Informe o valor de B: ").replace(",","."))
                    c = float(input("Informe o valor de C: ").replace(",","."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.segundo_grau(a, b, c)
                    for x in result:
                        print(x)
                    continue
                case "3":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Operação Inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível calcular. {e}.")
            continue