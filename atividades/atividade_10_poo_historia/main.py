"""
# TODO - atividade: Crie um programa que receba os dados de dois objetos diferentes da mesma classe Pessoa. Os dados serão os seguintes:
- Nome
- Idade 
- E-mail
- Telefone
- Gênero
- Tipo Sanguíneo
Supunho que o objeto 'usuario_2' esteja precisando de doação de sangue do 'usuario_1'. O programa deve informar os dados dos dois usuários, e ao final, informar se o usuário pode doar sangue para o usuário_2 ou não.
# NOTE - as duas últimas perguntas deverá ter uma resposta randômica.
"""
import random

class Individuos:
    def __init__(self, nome, idade, email, telefone, genero, tipo_sanguineo, convencimento):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.tipo_sanguineo = tipo_sanguineo
        self.convencimento = convencimento

    # metodos
    def dar_boas_vindas(self):
        return "Boa tarde!"
    
    def perguntar(self):
        return f"Qual o seu nome?"
    
    def cumprimentar_vamp(self):
        return f"Olá, eu me chamo {self.nome}. É uma honra!"
    
    def cumprimentar(self):
        return f"Oie, eu me chamo {self.nome},"

    def pergunta_sangue(self):
        return f"Qual o seu tipo sanguineo?"
    
    def resposta_mulher(self):
        return f"dsadad"

    def contexto_vampiro(self):
        return f"Então se você não doar seu sangue pra mim irei de vasco, eu sou um vampiro você pode me ajudar?"
        
    def ofender(self, nome):
        return f"{nome} seu esquisito!!! Some daqui! Vai ver se eu tô na esquina! TEM UM DOIDO AQUI!!!"
    
    def corre(self):
        print("(O vampiro corre pra muito longe...)")
    
    def cartao_de_vampiro(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"Tipo Sanguineo: {self.tipo_sanguineo}")
        print(f"Gênero: {self.genero}")

lista_de_tipos_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O", "O-"]

if __name__ == "__main__":
    # instancia de dois objetos
    usuario_vampiro = Individuos("", "", "", "", "", random.choice(lista_de_tipos_sanguineo), bool(random.getrandbits(1)))
    usuario_feminino = Individuos("", "", "", "", "", random.choice(lista_de_tipos_sanguineo), bool(random.getrandbits(1)))

    # seta os valores dos atributos do objeto masculino
    usuario_vampiro.nome = input("Informe seu nome: ").title().strip()
    usuario_vampiro.email = input("Informe seu email: ").strip()
    usuario_vampiro.idade = int(input("Informe sua idade: "))
    usuario_vampiro.telefone = input("Informe seu telefone: ").strip()
    usuario_vampiro.genero = input("Informe seu genero: ").strip()


    '''
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.tipo_sanguineo = tipo_sanguineo
        self.convencimento = convencimento
    '''

    # seta os valores dos atributos do objeto feminino
    usuario_feminino.nome = input("Informe seu nome: ").title().strip()
    usuario_feminino.email = input("Informe seu email: ").strip()

    # conversas
    print(f"???: -{usuario_vampiro.dar_boas_vindas()}")
    print(f"Mulher: -{usuario_feminino.dar_boas_vindas()}")
    print(f"???: -{usuario_vampiro.perguntar()}")
    print(f"Mulher: -{usuario_feminino.cumprimentar()}")
    print(f"Mulher: -{usuario_feminino.perguntar()}")
    print(f"???: -{usuario_vampiro.cumprimentar_vamp()}")
    print(f"???: -{usuario_vampiro.pergunta_sangue()}")
    # ela responde
    print(f"Vampiro: -{usuario_vampiro.contexto_vampiro()}")
    if usuario_feminino.convencimento is True:
        print(f"Vampiro: -{usuario_vampiro.cumprimentar()}")
        
        print("Segue meu cartão de vampiro:")
        print(usuario_vampiro.cartao_de_visitas())
    else:
        print(f"Mulher: -{usuario_feminino.ofender()}")
        usuario_vampiro.corre = usuario_feminino.convencimento