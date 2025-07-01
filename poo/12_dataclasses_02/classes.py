from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, trabalho como {self.profissao}, meu CPF é {self.cpf}, meu e-mail é {self.email}, meu telefone é {self.telefone} e meu endereço é {self.endereco}."
    
    def __del__(self):
        print(f"Objeto {self.nome} destruido com sucesso.")
    
@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        return f"Somos a empresa {self.nome_fantasia}, de razão social {self.razao_social}, nosso cnpj é {self.cnpj}, nosso e-mail de contato é {self.email}, nosso telefone é {self.telefone} e vá ao nosso endereço {self.endereco}."
    
    def __del__(self):
        print(f"Objeto {self.nome_fantasia} destruido com sucesso.")