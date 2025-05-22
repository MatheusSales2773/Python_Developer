'''
Faça um programa que receba o nome e a média final de um aluno, e o programa retorna se o aluno foi aprovado, se ficou de recuperação, ou se foi aprovado, com base em sua média final
'''
# NOTE - a média deverá ser entre 0 e 10
# NOTE - média para aprovação = 7. Recuperação = 5.

# declarando de variáveis
nome_aluno = input("Nome do Aluno: ")
media = float(input("Insira a média final: ").replace(",", "."))

if media >= 0 and media <=10: 
    if media >=7:
        print(f"O aluno {nome_aluno} está aprovado")
    elif media >= 5:
        print(f"O aluno {nome_aluno} está de recuperação")
    else:
        print(f"O aluno {nome_aluno} está reprovado")

else:
    print("Valor inválido.")
