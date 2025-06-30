from classes import Aluno, Curso 
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":

    alunos = []
    cursos = []
    matricula = 0

    limpar()
    while True:
        aluno = Aluno(nome="", matricula=0, cpf="")
        curso = Curso(nome_curso="")

        print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}")
        print("1 - Cadastrar Aluno.")
        print("2 - Cadastrar Curso.")
        print("3 - Matrícular Aluno.")
        print("4 - Listar Cursos.")
        print("5 - Listar Alunos.")
        print("6 - Sair do programa.")
        print('-'*65)

        opcao = input("Informe a opção desejada: ").strip()

        limpar()
        match opcao:
            case "1":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do aluno: ").strip().title()
                    aluno.cpf = input("Informe o CPF do aluno: ").strip()
                    aluno.matricula = matricula

                    alunos.append(aluno)
                    limpar()

                    print(f"Aluno {aluno.nome} matrículado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível cadastrar o aluno. {e}")
                finally:
                    continue

            case "2":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do curso: ").strip().title()
                    aluno.cpf = input("Informe o CPF do aluno: ").strip()
                    aluno.matricula = matricula

                    alunos.append(aluno)
                    limpar()

                    print(f"Curso {curso.nome} adicionado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível cadastrar o curso. {e}")
                finally:
                    continue
                
            case "3 ":
                try:
                    print(f"{'-'*10} Lista Alunos {'-'*10}")
                    for aluno in alunos:
                        print(f"Nome:{aluno.nome}")
                        print(f"Matrícula: {aluno.matricula}")
                        print(f"CPF: {aluno.cpf}")
                    inscricao = int(input("Informe a matrícula: "))
                    for aluno in alunos:
                        aluno = {
                            'nome': aluno.nome,
                            'matricula': aluno.matricula,
                            'cpf': aluno.cpf
                        }
                        if inscricao in alunos['matricula']:
                            break
                        else:
                            ...

                    limpar()

                    print(f"{'-'*10} Lisat de cursos {'-'*10}")
                    for curso in cursos:
                        print(f"Curso: {curso.nome_curso}")
                    curso_inscricao = input("Informe o curso desejado: ").strip().title()

                    aluno.inscrever_curso(curso_inscricao) 
                    limpar()
                    print(f"Aluno {aluno.nome} Inscrito no curso {curso.nome_curso} com sucesso!!!")             

                except Exception as e:
                        print(f"Não foi matrícular o aluno no curso. {e}")
                finally:
                    continue
                

            case "4":
                cursos.nome_curso.sort()
                for curso in cursos:
                    print(f"curso: ")
                    print("Alunos:")
                    for aluno in curso.listar_alunos():
                        print(aluno)
                    print('-'*40)

            case "5":
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")
                    print(f"Matrícula: {aluno.matricula}")
                    print(f"CPF: {aluno.cpf}")
                    print("Cursos matriculados: ")
                    for curso in aluno.listar_cursos():
                        print(curso)
                    print('-'*40)
                    
            case "6":
                print("Encerrando programa")
                break
            case _:
                print(f"Não foi possível continuar a execução.{e}.")
            
'''
    # instancia dos alunos
        aluno1 = Aluno("Fulano", 101, "111.111.111-11")
        aluno2 = Aluno("Cicrano", 102, "222.222.222-22")
        aluno3 = Aluno("Beltrano", 103, "561.241.660-11")
        aluno4 = Aluno("João", 104, "939.807.900-37")
        aluno5 = Aluno("Matheus", 105, "314.701.810-53")
        aluno6 = Aluno("Vini", 106, "087.435.920-15")
        aluno7 = Aluno("Julia", 107, "597.475.660-60")
        aluno8 = Aluno("Alex", 108, "652.640.640-83")
        aluno9 = Aluno("Caua", 109, "842.743.170-80")
        aluno10 = Aluno("Nicolly", 110, "739.933.970-88")

        # instancia dos cursos
        curso1 = Curso("Python Developer")
        curso2 = Curso("IA com Python")
        curso3 = Curso("Desenvolvedor Ruby")

        # inscrevendo os alunos no curso 1
        aluno1.inscrever_curso(curso1)
        aluno2.inscrever_curso(curso1)
        aluno3.inscrever_curso(curso1)    
        aluno4.inscrever_curso(curso1)
        aluno5.inscrever_curso(curso1)

        # inscrevendo os alunos no curso 2
        aluno6.inscrever_curso(curso2)
        aluno7.inscrever_curso(curso2)
        aluno8.inscrever_curso(curso2)

        # inscrevendo os alunos no curso 3
        aluno9.inscrever_curso(curso3)
        aluno10.inscrever_curso(curso3)

        print(f"O curso '{curso1.nome_curso}' Tem os Alunos: {curso1.listar_alunos()}")
'''