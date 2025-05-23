"""
Crie um programa que receba o nome, o peso e a altura do usuário, e informe seu IMC (Índice de Massa Corporal) e informe seu diagnóstico de acordo com o valor de seu IMC:
- Magro demais
- Peso Normal
- Acima do peso
- Obeso
- Obesidade nível II
- Obesidade mórbida
"""

while True:
    # variáveis
    nome = input("Coloque seu nome: ")
    altura = float(input("Qual sua altura(metros): ").replace(",", "."))
    peso = float(input("Qual seu peso(kg): ").replace(",", "."))

    # IMC
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    # Diagnóstico
    if imc < 18.5:
        print("Magro demais")
    elif 18.5 <= imc < 24.9:
        print("Peso Normal")
    elif 25 <= imc < 29.9:
        print("Acima do peso")
    elif 30 <= imc < 34.9:
        print("Obeso")
    elif 35 <= imc < 39.9:
        print("Obesidade nível II")
    else:
        print("Obesidade mórbida")

    # Pergunta se o usuário deseja escolher refazer o calculo 
    confirmação = input("Deseja fazer outro calcúlo de IMC? (s/n): ").strip().lower()

    # resposta da confirmação do usuário
    if confirmação in ["s", "sim", "ss"]:
        print("Insira novamente as informações")
    elif confirmação in ["n", "não", "nao"]:
        print(f"Obrigado pela preferência {nome}, espero que tenha ajudado")
        break
    else:        
        print("Opção inválida. Encerrando o programa.")
        break