from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    engine = create_engine("sqlite:///meu_primeiro_banco.")
    Base = declarative_base()

    # cria a entidade usuario
    class Pessoa(Base):
        # nome de entidade
        __tablename__ = "pessoa"

        # atributos
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        # FIXME data_nasc = Column(Date, nullable=False)
        email = Column(String, unique=True)
        cpf = Column(String, nullable=False, unique=True)
        genero = Column(String, nullable=False)
        tipo_sanguineo = Column(String, nullable=False)

    Base.metadata.create_all(engine)

    print("Entidade Pessoa criada com êxito")
except Exception as e:
    print(f"Erro ao criar motor. {e}.")
    
try:
    Session = sessionmaker(bind=engine)
    session = Session()

    # cadastrar o usuário no banco
    nome = input("Informe o nome: ").strip().title()
    # FIXME data_nasc = input("Informe a data de Nascimento: (aaaa-mm-dd): ").strip()
    email = input("Informe o email: ").strip()
    cpf = input("Informe o cpf: ").strip()
    genero = input("Informe o genero: ").strip()
    tipo_sanguineo = input("Informe o tipo sanguíneo: ").strip().upper()

    nova_pessoa = Pessoa(
        nome=nome,
        # FIXME data_nasc=data_nasc,
        email=email,
        cpf=cpf,
        genero=genero,
        tipo_sanguineo= tipo_sanguineo
    )

    session.add(nova_pessoa)
    session.commit()

    print("Pessoa cadastrada com sucesso")

    session.close()
except Exception as e:
    print(f"Erro ao criar motor. {e}.")