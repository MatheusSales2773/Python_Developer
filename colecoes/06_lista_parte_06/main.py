import os

nomes = [
    "Fulano",
    "Beltrano",
    "Cicrano",
    "Robert",
    "Alex",
    "Adam",
    "Luis",
    "José",
    "Eva",
    "Pedro"
]

# exibe lista
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}.")
# usuário informa a posição da lsita que deseja excluir
try:
    print("\n")
    i = int(input("Informe o índicice que deseja excluir: "))
    os.system("cls")

    if i >= 0 and i < len(nomes):
        print (f"Item a ser excluido: {nomes[i]}")
        confirma = input(f"Deseja excluir {nomes[i]}? (s/n) ").lower().strip()
        os.system("cls")
        match confirma:
            case "s":
                del(nomes[i])
                print("Item excluido com sucesso.")
            case "n":
                print(f"{nomes[i]} não será excluído.")
            case _:
                print("Opção inválida")
    else:
        print("Índice inválido")
except Exception as e:
    print(f"Não foi possível excluir item. {e}.")
finally:
    print(f"Nova lista: \n")
    for i in range(len(nomes)):
        print(f"Índice {i}: {nomes[i]}.")