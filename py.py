
tarefas = []


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso.')


def remover_tarefa():
    tarefa = input("Digite a tarefa a ser removida: ")
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f'Tarefa "{tarefa}" removida com sucesso.')
    else:
        print("Tarefa não encontrada.")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            remover_tarefa()
        elif escolha == "3":
            listar_tarefas()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
