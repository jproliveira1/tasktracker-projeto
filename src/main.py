"""
TaskTracker - Aplicação CLI em Python (Fase 2)
Autor: João Pedro Rezende Oliveira
Descrição: Sistema de gerenciamento de tarefas estruturado a partir do planejamento lógico.
"""

def exibir_menu():
    """Exibe o menu principal de navegação da aplicação."""
    print("\n========================================")
    print("           TASKTRACKER - MENU           ")
    print("========================================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("========================================")


def cadastrar_tarefa(lista_tarefas):
    """Realiza o cadastro de uma nova tarefa com validação estrita dos campos."""
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    
    # 1. Validação do Título (Obrigatório e não vazio)
    while True:
        titulo = input("Digite o Título da tarefa: ").strip()
        if not titulo:
            print("[ERRO] O título não pode ser vazio ou conter apenas espaços. Tente novamente.")
        else:
            break

    # 2. Demais campos opcionais ou livres conforme planejamento
    descricao = input("Digite a Descrição (opcional): ").strip()
    
    # 3. Validação estrita da Prioridade (Alta, Média/Media, Baixa)
    while True:
        prioridade = input("Digite a Prioridade (Alta / Média / Baixa): ").strip().capitalize()
        # Normaliza acentuação comum se o usuário digitar sem acento
        if prioridade == "Media":
            prioridade = "Média"
            
        if prioridade in ["Alta", "Média", "Baixa"]:
            break
        else:
            print("[ERRO] Prioridade inválida! Escolha estritamente entre: Alta, Média ou Baixa.")

    data_limite = input("Digite a Data Limite (padrão DD/MM/AAAA 24HH:MM): ").strip()
    categoria = input("Digite a Categoria (opcional): ").strip()
    estimativa = input("Digite a Estimativa de tempo para conclusão (opcional): ").strip()

    # Criação do dicionário representando a tarefa
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "categoria": categoria if categoria else "Geral",
        "estimativa": estimativa if estimativa else "Não informada",
        "status": "Pendente"  # Regra: Toda tarefa nasce com status Pendente
    }

    # Adiciona à lista
    lista_tarefas.append(nova_tarefa)
    print(f"\n[SUCESSO] Tarefa '{titulo}' cadastrada com sucesso!")


def visualizar_tarefas(lista_tarefas):
    """Exibe a lista de tarefas cadastradas ou avisa se estiver vazia."""
    print("\n--- LISTA DE TAREFAS CADASTRADAS ---")
    
    # Regra de verificação de lista vazia
    if not lista_tarefas:
        print("Aviso: Nenhuma tarefa cadastrada no momento.")
        return

    # Exibição iterativa das tarefas
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        print(f"\n[{indice}] Título: {tarefa['titulo']}")
        print(f"    Descrição: {tarefa['descricao']}")
        print(f"    Prioridade: {tarefa['prioridade']}")
        print(f"    Data Limite: {tarefa['data_limite']}")
        print(f"    Categoria: {tarefa['categoria']}")
        print(f"    Estimativa: {tarefa['estimativa']}")
        print(f"    Status: {tarefa['status']}")
    print("-" * 40)


def main():
    """Função principal que gerencia o fluxo de execução do programa."""
    tarefas = []
    
    print("Bem-vindo ao TaskTracker!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até a próxima!")
            break
        else:
            print("\n[ERRO] Opção inválida! Por favor, escolha um número entre 1 e 3.")


if __name__ == "__main__":
    main()