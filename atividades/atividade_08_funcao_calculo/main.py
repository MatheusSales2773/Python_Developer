'''
TODO - atividade: Crie um Programa Onde o Usuário Possa Fazer as seguintes operações:
     - Calcular área de um quadrado
     - Calcular área de um retângulo
     - Calcular área de um triângulo
     - Calcular área de um trapézio
     - Sair do programa

'''

# importando o math e os

import os

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Funções Para Facilitar o Código

def clear():
    os.system("cls")


def back():
    input("Pressione Qualquer Tecla para Voltar: ")
    clear()

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Funções de Calculo

def calcular_quadrado(lado):
    area = lado * lado
    clear()
    print(f"A área do quadrado é: {area}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------

def calcular_retangulo(base, altura):
    area = base * altura

    print(f"A área do Retângulo é: {area}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------

def calcular_triangulo(baset, alturat):

    areat = baset * alturat / 2

    print(f"A área do Triângulo é: {areat}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------

def area_trapezio(base_maior, base_menor, alturaz):

    areaz = (base_maior + base_menor) * alturaz / 2

    print(f"A área do Trapézio é: {areaz}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Menu 

while True:
    print('-'*24, "Calculo De Áreas", '-'*24)
    print("1 - Calcular a área de um quadrado")
    print("2 - Calcular a área de um retângulo")
    print("3 - Calcular a área de um triângulo")
    print("4 - Calcular a área de um trapézio")
    print("5 - Sair do programa")
    print('-'*59)

    print("")

    opcao = input("Escolha uma Opção: ").strip()

    match opcao:
        case "1":
            clear()
            print('-'*24, "Calcular a Área de um Quadrado", '-'*24)
            print("")
            try:
                lado = float(input("Informe o Lado do Quadrado: "))
                calcular_quadrado(lado)
            except Exception:
                print("Insira um valor Válido")
            finally:
                print("")
                back()
                clear()
                continue
        case "2":
            clear()
            print('-'*24, "Calcular Retângulo", '-'*24)
            print("")
            try:
                base = float(input("Informe o Valor da Base: "))
                altura = float(input("Informe o Valor da Altura: "))

                print("")

                calcular_retangulo(base, altura)

            except Exception:
                print("Não Foi Possível Calcular")

            finally:
                print("")
                back()
                clear()
                continue

        case "3":
            clear()
            print('-'*24, "Calcular Triângulo", '-'*24)
            print("")

            try:
                baset = float(input("Informe o Valor da Base: "))
                alturat = float(input("Informe o Valor da Altura: "))

                print("")

                calcular_triangulo(baset, alturat)
            except Exception:
                print("Não Foi Possível Concluir o Calculo")
            finally:
                print("")
                back()
                clear()
                continue
        case "4":
            clear()
            print('-'*24, "Calcular área de um Trapézio", '-'*24)
            print("")

            try:
                base_maior = float(input("Informe o Valor da Base Menor: "))
                base_menor = float(input("Informe o Valor da Base Menor: "))
                alturaz = float(input("Informe o Valor da Altura: "))

                print("")
                
                area_trapezio(base_maior, base_menor, alturaz)
            except Exception:
                print("Não Foi Possível Concluir o Calculo")
            finally:
                print("")
                back()
                clear()
                continue
        case "5":
            clear()
            break
        case _:
            clear()
            print("Opção Inválida")
            back()
            clear()
            continue
