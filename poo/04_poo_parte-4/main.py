import random 
import os

# classe
class Pessoa:
    #construtor
    def __init__(self, nome, email, profissao, humor):
        self.nome = nome
        self.email = email
        self.profissao = profissao
        self.humor = humor

    # metodos
    def dar_boas_vindas(self):
        return "Boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. É uma honra!"
    
    def perguntar(self):
        return f"Qual o seu nome?"
    
    def cartao_de_visitas(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Profissão: {self.profissao}")

    def ofender(self, nome):
        return f"Quem liga {nome}? Me erra! Vai ver se eu tô na esquina!"

if __name__ == "__main__":
    # instancia de dois objetos
    usuario_masculino = Pessoa("", "", "", bool(random.getrandbits(1)))
    usuario_feminino = Pessoa("", "", "", bool(random.getrandbits(1)))

    # seta os valores dos atributos do objeto masculino
    usuario_masculino.nome = input("Informe seu nome: ").title().strip()
    usuario_masculino.email = input("Informe seu email: ").strip()
    usuario_masculino.profissao = input("Informe sua profissao: ").title().strip()

    # seta os valores dos atributos do objeto feminino
    usuario_feminino.nome = input("Informe seu nome: ").title().strip()
    usuario_feminino.email = input("Informe seu email: ").strip()
    usuario_feminino.profissao = input("Informe sua profissao: ").title().strip()

    # conversas
    print(f"Homem: -{usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: -{usuario_feminino.dar_boas_vindas()}")
    print(f"Homem: -{usuario_masculino.perguntar()}")
    if usuario_feminino.humor is True:
        print(f"Mulher: -{usuario_feminino.cumprimentar()}")
        print(f"Mulher: -{usuario_feminino.perguntar()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homem: -{usuario_feminino.cumprimentar()}")
        print(f"Homem: Bom humor = {usuario_masculino.humor}")
        print("Segue meu cartão de visitas: ")
        print(usuario_masculino.cartao_de_visitas())
    else:
        print(f"Mulher: -{usuario_feminino.ofender()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homem: Bom humor = {usuario_masculino.humor}")