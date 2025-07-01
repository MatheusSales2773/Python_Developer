from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade=0,
        email="",
        telefone="",
        profissao="",
        peso=0.0,
        altura=0.0
    )

    usuario.nome = "Caça-Rato"
    usuario.idade = 28
    usuario.email = "fulano@gmail.com"
    usuario.telefone = "(61)99999-9999"
    usuario.profissao = "programador"
    usuario.peso = 100
    usuario.altura = 1.85

    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"Email: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Profissão: {usuario.profissao}")
    print(f"peso: {usuario.peso}")
    print(f"Altura: {usuario.altura}")
