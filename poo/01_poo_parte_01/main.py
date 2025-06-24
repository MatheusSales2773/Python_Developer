# classe
class Pessoa:
    # atributos da classe
    nome = "Matheus Sales"
    idade = 19
    email = "matheus@gmail.com"
    profissao = "programador"

# algoritmo principal
if __name__ == "__main__":
        # instanciar a classe Pessoa(vai criar objeto da classe)
        usuario = Pessoa()

        # exibe na tela os dados do usuário
        print(f"Nome: {usuario.nome}.")
        print(f"Idade: {usuario.idade}.")
        print(f"Email: {usuario.email}.")
        print(f"Profissão: {usuario.profissao}.")

