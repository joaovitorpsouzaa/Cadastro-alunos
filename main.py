alunos = []
def cadastrar():
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio.")
        return
    for aluno in alunos:
        if aluno.lower() == nome.lower():
            print("Aluno já cadastrado.")
            return
    alunos.append(nome)
    print("Aluno cadastrado.")

def listar():
    for aluno in alunos:
        print(aluno)
while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    else:
        print("Opção inválida.")