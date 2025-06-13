'''
# TODO - atividade: Crie im programa que receba do usuário os seguitnes dados:
- Nome
- CPF
- Data de nascimento
- E-mail
- Gênero
- Telefone
- Endereço
- Altura em metros
- Pesos em Kg
- Tipo sanguineo

Ao final, o programa exibe esses dados
'''

import os

pessoa = {
    'nome': "",
    'cpf': "",
    'data_nascimento': "",
    'email': "",
    'genero': "",
    'telefone': "",
    'endereço': "",
    'altura': "",
    'peso': "",
    'tipo_sanguineo':  ""
}

try:
    pessoa['nome'] = input("Informe o nome: ").title().strip()
    pessoa['cpf'] = input("Informe o cpf: ").strip()
    pessoa['data_nascimento'] = input("Informe a Data de Nascimento: ").strip()
    pessoa['email'] = input("Informe o email: ").strip()
    pessoa['genero'] = input("Informe o genero(M/F/Outro): ").strip().capitalize()
    pessoa['telefone'] = input("Informe o telefone: ").strip()
    pessoa['endereço'] = input("Informe o endereço: ").strip()
    pessoa['altura'] = float(input("Informe o altura: ").replace(",",".").strip())
    pessoa['peso'] = float(input("Informe o peso: ").replace(",",".").strip())
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguíneo (ex: O+, AB-): ").strip().upper()

except ValueError:
    print("Erro de conversão numérica. Verifique os dados de altura/peso.")
    exit()

except Exception as e:
    print(f"Não foi possível continuar o processo {e}")
    exit()
    
os.system("cls")

print(f"Nome: {pessoa['nome']}")
print(f"cpf: {pessoa['cpf']}")
print(f"data_nascimento: {pessoa['data_nascimento']}")
print(f"email: {pessoa['email']}")
print(f"genero: {pessoa['genero']}")
print(f"telefone: {pessoa['telefone']}")
print(f"endereço: {pessoa['endereço']}")
print(f"altura: {pessoa['altura']}")
print(f"peso: {pessoa['peso']}")
print(f"Tipo sanguineo: {pessoa['tipo_sanguineo']}")