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
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- ALUNOS ---")
    for numero, aluno in enumerate(alunos, start=1):
        print(f"{numero}. {aluno}")
        print(f"Total: {len(alunos)} aluno(s)")

def buscar():
    termo = input("Nome completo para buscar: ").strip()
    if termo == "":
        print("Digite um nome para buscar.")
        return
    for aluno in alunos:
        if aluno.lower() == termo.lower():
            print(f"Encontrado: {aluno}")
            return
        print("Aluno não encontrado.")

while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("0 - Sair")

    opcao = input("Escolha: ")
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    else:
        print("Opção inválida.")