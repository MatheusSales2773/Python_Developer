# declaração de kusta
carrinho = []

while True:
    print('-'*20, 'Carrinho de Compra', '-'*20)

    item = input("Informe um item: ").capitalize().strip() # capitalize é um método de string que coloca a primeira letra em maiúscula e o resto da string em minúscula.
    carrinho.append(item)

    print(f"{item} inserido no carrinho com sucesso ")
    confirmar = input("Deseja inserir outro item? (s/n) ").lower().strip()
    

    match confirmar:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            continue

# ordena a lista em ordem alfabética
carrinho.sort()

# exibe os itens da lista
for item in carrinho:
    print(item)