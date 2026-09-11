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
while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    else:
        print("Opção inválida.")