

# declarando de variáveis
nome = input("Coloque o nome do usuário: ")
idade =  int(input("A idade do usuário é: "))
altura = float(input("A altura do usuário é: ").replace(",", "."))

# verifica a idade e a altura do usuário
if idade >= 12 and altura >= 1.20:
    print(f"A entrada de {nome} foi autorizada, catraca liberada.")
else:
    print(f"A entrade de {nome} não foi autorizada, catraca não liberada.")

