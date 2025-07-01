# importações
from dataclasses import dataclass

@dataclass
class Pessoa:
    #atributos
    nome: str
    idade: int
    email: str
    telefone:str
    peso: float
    altura: float

    def __str__(self):
        return f"Olá, meu nome é {self.nome}."
    
    # def __len__(self):
        
    def __del__(self):
        print(f"Objeto {self.nome} destruido com sucesso.")