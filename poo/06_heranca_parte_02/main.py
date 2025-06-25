import classes

if __name__ == "__main__":
    filho = classes.Filho("", "", "", "", 0.0, 0.0)

    try:

        filho.nome = input("Informe o Nome: ").strip().title()
        filho.email = input("Informe o Email: ").strip()
        filho .telefone = input("Informe o Telefone: ").strip()
        filho.genero = input("Informe o Gênero: ").title().strip()
        filho.peso = float(input("Informe o Peso: ").replace(',','.'))
        filho.altura = float(input("Informe a Altura: ").replace(',','.'))

        filho.exibir_info()

    except Exception as e:
        print(e)
