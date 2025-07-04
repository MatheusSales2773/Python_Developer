"""
# TODO = atividade 11: crie um programa que exiba um menu com seguintes operações:
- Cadastrar um novo usuário no banco
- Listar todos os usuários do banco
- Sair do programa
# NOTE - a entidade deverá ser gerada pelo python
# NOTE - nome do banco: db_atividade_10. Entidade Usuário.
Atributos:
- Nome
- CPF
- E-mail
- Data de Nascimento
- Telefone
- Profissão
- Endereço
- Altura
- Peso
"""

from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

try:

    engine = create_engine("sqlite:///db_atividade_10.db")
    Base = declarative_base()

    class Usuario(Base):
        __tablename__ = "usuario"

        id_usuario = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        cpf = Column(String, unique=True)
        email = Column(String, unique=True)
        data_de_nascimento = Column(Date, nullable=False)
        telefone = Column(String, nullable=False)
        profissao = Column(String, nullable=False)
        endereco = Column(String, nullable=False)
        altura = Column(Float, nullable=False)
        peso = Column(Float, nullable=False)

    Base.metadata.create_all(engine)
    print("Entidade Usuario criada com êxito")

except Exception as e:
    print(f"Não foi possível cadastrar uma pessoa no banco. {e}.")

limpar()

if __name__ == "__main__":
    while True:
        print('-'*24, "Banco de dados - Usuário", '-'*24)
        print("1 - Cadastrar um novo usuário no banco")
        print("2 - Listar todos os usuários do banco")
        print("3 - Sair do Programa")
        print('-'*66)
        
        opcao = input("Informe a Opção Desejada: ").strip()
        os.system("cls")
        match opcao:
            case "1":
                
                try:
                    Session = sessionmaker(bind=engine)
                    session = Session()

                    # cadastrar o usuário no banco
                    nome = input("Informe o nome: ").strip().title()
                    cpf = input("Informe o cpf: ").strip()
                    email = input("Informe o email: ").strip()
                    data_de_nascimento = input("Informe a data de Nascimento: (dd-mm-aaaa): ").strip()
                    data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y").date()
                    telefone = input("Informe o seu telefone: ").strip()
                    profissao = input("Informe sua profissão: ").strip()
                    endereco = input("Informe o endereco: ")
                    altura = float(input("Informe a sua altura(Em metros): ").replace(",","."))
                    peso = float(input("Informe o seu peso(Em Kg): ").replace(",","."))

                    novo_usuario = Usuario(
                        nome=nome,
                        cpf=cpf,
                        email=email,
                        data_de_nascimento=data_de_nascimento,
                        telefone=telefone,
                        profissao=profissao,
                        endereco=endereco,
                        altura=altura,
                        peso=peso,
                    )

                    session.add(novo_usuario)
                    session.commit()

                    print("Usuario cadastrado com sucesso")

                except Exception as e:
                    limpar()
                    print(f"Erro ao criar engine. {e}.")

            case "2":
                limpar()
                Session = sessionmaker(bind=engine)
                session = Session()

                try:
                    usuarios = session.query(Usuario).all()

                    print(f"\n{'-'*20} USUÁRIOS CADASTRADOS {'-'*20}\n")
                    for usuario in usuarios:
                        print(f"ID: {usuario.id_usuario}") 
                        print(f"Nome: {usuario.nome}")
                        print(f"CPF: {usuario.cpf}")
                        print(f"E-mail: {usuario.email}") 
                        print(f"Data de Nascimento: {usuario.data_de_nascimento.strftime("%d/%m/%Y")}") 
                        print(f"Telefone: {usuario.telefone}") 
                        print(f"Profissão: {usuario.profissao}") 
                        print(f"Endereço: {usuario.endereco}") 
                        print(f"Altura: {usuario.altura}") 
                        print(f"Peso: {usuario.peso}") 
                        print('-'*72)
                        print()

                    session.close()

                except Exception as e:
                    print("")
                    limpar()
                    print(f"Erro ao procurar usuários. {e}.")

                finally:
                    print("")
                    input("Aperte ente para continuar...")
                    limpar()  

            case "3":
                print("Encerrando programa.")
                break
            case _:
                print("Opção invalida")
                limpar()
                continue