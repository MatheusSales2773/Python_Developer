# lista 
import os

frutas = [
    'Morango',
    'Banana',
    'Maçã',
    'Pera',
    'Uva',
    'Maracujá',
    'Abacaxi',
    'Laranja',
    'Pessêgo'
]

# exibe a lista com seus respectivos indices

for i in range(len(frutas)):
    print(f"Indice {i}: {frutas[i]}")

# usuario informa o indice da fruta deseja alterar
try:
    i = int(input("Informe o número do índice a ser alterado: "))
    os.system("cls")
    if i >= 0 and i < len(frutas):
        print(f"Valor encontrado: {frutas[i]}")
        frutas[i] = input("Informe o nome da nova fruta: ")
        os.system("cls")
        print("Fruta alterada com sucesso.\n")
    else:
        print("Valor do índice inválido.")
except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")
finally:
    print("Nova lista")
    for i in range(len(frutas)):
        print(f"índice {i}: frutas {frutas[i]}.")