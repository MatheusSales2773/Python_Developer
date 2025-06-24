# classe
class Pessoa:
    # atributos da classe
    nome = "Matheus Sales"
    idade = 19
    email = "matheus@gmail.com"
    profissao = "programador"

    # métodos
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, trabalho como {self.profissao} e meu e-mail é {self.email}")

# algoritmo principal
if __name__ == "__main__":
    # instancia a classe
    usuario = Pessoa()

    # executar o método
    usuario.apresentar()