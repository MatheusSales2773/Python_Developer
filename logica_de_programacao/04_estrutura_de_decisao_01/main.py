nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: ")) # adiciona int na frente do input para recber um número inteiro

# saída de dados
if idade >= 18:
    print(f"Seu nome é {nome} e voce é maior de idade possuindo {idade} anos")
else:
    print(f"Seu nome é {nome} e voce é menor de idade possuindo {idade} anos")