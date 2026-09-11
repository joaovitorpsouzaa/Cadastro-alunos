alunos = []
def cadastrar():
    nome = input("Nome do aluno: ")
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