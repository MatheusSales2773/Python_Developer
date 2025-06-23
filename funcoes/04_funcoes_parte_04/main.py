import os
import math as m

def mostrar_pi():
    return f"{m.pi:.2f}"

def calcular_circuferencia(r):
    c = 2*m.pi*r
    return c

def area_circulo(r):
    a = m.pi*r**2
    return a

while True:
    print('-'*24, "Exercício", '-'*24)
    print("1 - Mostrar Número PI")
    print("2 - Calcular Tamanho da Circuferência")
    print("3 - Calcular Área do Círculo")
    print("4 - Sair do Programa")
    print('-'*66)
    print("")

    opcao = input("Informe a Opção Desejada: ").strip()

    os.system("cls")

    try:
        if opcao == "2" or opcao == "3":
            r = float(input("Informe o Valor do Raio: ")).replace(',','.')
        else:
            pass

    except Exception as e:
        print(f"Não Foi Possível Executar o Cálculo. Error: {e}")
    
    match opcao :
        case "1":
            os.system("cls")
            print('-'*24, "Mostrando PI", '-'*24)
            print(f"Numero do PI: {mostrar_pi()}")
            print("")
            input("Aperte Qualquer Tecla Para Continuar: ")
            os.system("cls")
            continue
        case "2":
            os.system("cls")
            print('-'*24, "Calculando Circuferência", '-'*24)
            print(f"Circuferência: {calcular_circuferencia(r)}")
            input("Aperte Qualquer Tecla Para Continuar: ")
            os.system("cls")
            continue
        case "3":
            os.system("cls")
            print('-'*24, "Calculando Circuferência", '-'*24)
            print(f"Área do Círculo: {area_circulo(r)}")
            input("Aperte Qualquer Tecla Para Continuar: ")
            os.system("cls")
            continue
        case "4":
            os.system("cls")
            break
        case _:
            os.system("cls")
            print("Operação Inválida")
            input("Aperte Qualquer Tecla Para Continuar: ")
            os.system("cls")
            continue