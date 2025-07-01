from dataclasses import dataclass
from abc import ABC
from abc import abstractmethod

@dataclass
class Pessoa(ABC):
    email: str
    telefone: str
    endereco: str

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    profissao: str
    genero: str

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, trabalho como {self.profissao}, meu gênero é {self.genero}, meu e-mail é {self.email}, meu telefone é {self.telefone} e meu endereço é {self.endereco}."
    
    def __len__(self): # pegadinha
        pass

    def __del__(self):
        print(f"Objeto {self.nome} obliterado com sucesso")
    
    def exibir_dados(self):
        print(f"Nome da empresa: {self.nome}")
        print(f"Profissão: {self.profissao}")
        print(f"Gênero: {self.genero}")
        super().exibir_dados()

@dataclass
class PessoaJuridica(Pessoa):
    cnpj: str
    nome_fantasia: str
    website: str

    def __str__(self):
        return f"Somos a empresa {self.nome_fantasia}, conheça nosso website {self.website}, nosso cnpj é {self.cnpj}, nosso e-mail de contato é {self.email}, nosso telefone é {self.telefone} e vá ao nosso endereço {self.endereco}."
    
    def __len__(self): # pegadinha
        pass
    
    def __del__(self):
        print(f"Objeto {self.nome_fantasia} destruido com sucesso.")

    def exibir_dados(self):
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Website: {self.website}")
        super().exibir_dados()