# declaração de variáveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade"))

# ternario
result = "é maior de idade." if idade >=18 else "é menor de idade."

# saída de dados
print(f"{nome} {result}")