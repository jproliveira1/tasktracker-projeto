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
    print("2. Visualizar tarefas cadastradas (Ordenadas)")
    print("3. Concluir uma tarefa")
    print("4. Atualizar dados de uma tarefa")
    print("5. Sair da aplicação")
    print("========================================")


def cadastrar_tarefa(lista_tarefas):
    """Realiza o cadastro de uma nova tarefa com validação estrita dos campos."""
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    
    # 1. Validação do Título (Obrigatório e não vazio)[cite: 19]
    while True:
        titulo = input("Digite o Título da tarefa: ").strip()
        if not titulo:
            print("[ERRO] O título não pode ser vazio ou conter apenas espaços. Tente novamente.")
        else:
            break

    # 2. Demais campos opcionais ou livres conforme planejamento[cite: 22]
    descricao = input("Digite a Descrição (opcional): ").strip()
    
    # 3. Validação estrita da Prioridade (Alta, Média/Media, Baixa)[cite: 19]
    while True:
        prioridade = input("Digite a Prioridade (Alta / Média / Baixa): ").strip().capitalize()
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
        "status": "Pendente"  # Regra: Toda tarefa nasce com status Pendente[cite: 19]
    }

    # Adiciona à lista
    lista_tarefas.append(nova_tarefa)
    print(f"\n[SUCESSO] Tarefa '{titulo}' cadastrada com sucesso!")


def visualizar_tarefas(lista_tarefas):
    """Exibe a lista de tarefas ordenadas por prioridade ou avisa se estiver vazia."""
    print("\n--- LISTA DE TAREFAS CADASTRADAS (ORDENADAS) ---")
    
    # Regra de verificação de lista vazia[cite: 19]
    if not lista_tarefas:
        print("Aviso: Nenhuma tarefa cadastrada no momento.")
        return

    # Dicionário de pesos para definir a hierarquia de ordenação (Alta > Média > Baixa)
    peso_prioridade = {
        "Alta": 1,
        "Média": 2,
        "Baixa": 3
    }

    # Cria uma cópia da lista ordenada usando o peso da prioridade como critério
    tarefas_ordenadas = sorted(
        lista_tarefas, 
        key=lambda t: peso_prioridade.get(t['prioridade'], 4)
    )

    # Exibição iterativa das tarefas ordenadas
    for indice, tarefa in enumerate(tarefas_ordenadas, start=1):
        print(f"\n[{indice}] Título: {tarefa['titulo']}")
        print(f"    Descrição: {tarefa['descricao']}")
        print(f"    Prioridade: {tarefa['prioridade']}")
        print(f"    Data Limite: {tarefa['data_limite']}")
        print(f"    Categoria: {tarefa['categoria']}")
        print(f"    Estimativa: {tarefa['estimativa']}")
        print(f"    Status: {tarefa['status']}")
    print("-" * 40)


def concluir_tarefa(lista_tarefas):
    """Permite ao usuário selecionar uma tarefa pendente e alterar seu status para 'Concluído'."""
    print("\n--- CONCLUIR TAREFA ---")
    
    if not lista_tarefas:
        print("Aviso: Nenhuma tarefa cadastrada para ser concluída.")
        return

    visualizar_tarefas(lista_tarefas)
    
    while True:
        entrada = input("\nDigite o número da tarefa que deseja marcar como CONCLUÍDA (ou '0' para cancelar): ").strip()
        
        if not entrada.isdigit():
            print("[ERRO] Por favor, digite um número válido.")
            continue
            
        numero = int(entrada)
        
        if numero == 0:
            print("Operação de conclusão cancelada.")
            break
            
        if 1 <= numero <= len(lista_tarefas):
            # Nota: Para garantir consistência na seleção, mantemos a referência direta
            tarefa_selecionada = lista_tarefas[numero - 1]
            
            if tarefa_selecionada["status"] == "Concluído":
                print(f"[AVISO] A tarefa '{tarefa_selecionada['titulo']}' já está marcada como Concluída!")
            else:
                tarefa_selecionada["status"] = "Concluído"
                print(f"\n[SUCESSO] Tarefa '{tarefa_selecionada['titulo']}' foi marcada como CONCLUÍDA!")
            break
        else:
            print(f"[ERRO] Número inválido! Escolha um número entre 1 e {len(lista_tarefas)}.")


def atualizar_tarefa(lista_tarefas):
    """Permite ao usuário atualizar os dados de uma tarefa existente."""
    print("\n--- ATUALIZAR DADOS DA TAREFA ---")
    
    if not lista_tarefas:
        print("Aviso: Nenhuma tarefa cadastrada para ser atualizada.")
        return

    visualizar_tarefas(lista_tarefas)
    
    while True:
        entrada = input("\nDigite o número da tarefa que deseja ATUALIZAR (ou '0' para cancelar): ").strip()
        
        if not entrada.isdigit():
            print("[ERRO] Por favor, digite um número válido.")
            continue
            
        numero = int(entrada)
        
        if numero == 0:
            print("Operação de atualização cancelada.")
            break
            
        if 1 <= numero <= len(lista_tarefas):
            tarefa = lista_tarefas[numero - 1]
            print(f"\nEditando a tarefa: '{tarefa['titulo']}'")
            print("(Pressione ENTER sem digitar nada para manter o valor atual)")
            
            # Atualizar Título
            novo_titulo = input(f"Novo Título [{tarefa['titulo']}]: ").strip()
            if novo_titulo:
                tarefa['titulo'] = novo_titulo
                
            # Atualizar Descrição
            nova_desc = input(f"Nova Descrição [{tarefa['descricao']}]: ").strip()
            if nova_desc:
                tarefa['descricao'] = nova_desc
                
            # Atualizar Prioridade com validação estrita
            while True:
                nova_prio = input(f"Nova Prioridade (Alta/Média/Baixa) [{tarefa['prioridade']}]: ").strip().capitalize()
                if not nova_prio:
                    break
                if nova_prio == "Media":
                    nova_prio = "Média"
                    
                if nova_prio in ["Alta", "Média", "Baixa"]:
                    tarefa['prioridade'] = nova_prio
                    break
                else:
                    print("[ERRO] Prioridade inválida! Escolha estritamente entre: Alta, Média ou Baixa.")
                    
            # Atualizar Data Limite
            nova_data = input(f"Nova Data Limite [{tarefa['data_limite']}]: ").strip()
            if nova_data:
                tarefa['data_limite'] = nova_data
                
            # Atualizar Categoria
            nova_cat = input(f"Nova Categoria [{tarefa['categoria']}]: ").strip()
            if nova_cat:
                tarefa['categoria'] = nova_cat
                
            # Atualizar Estimativa
            nova_est = input(f"Nova Estimativa [{tarefa['estimativa']}]: ").strip()
            if nova_est:
                tarefa['estimativa'] = nova_est
                
            print(f"\n[SUCESSO] Tarefa atualizada com sucesso!")
            break
        else:
            print(f"[ERRO] Número inválido! Escolha um número entre 1 e {len(lista_tarefas)}.")


def main():
    """Função principal que gerencia o fluxo de execução do programa."""
    tarefas = []
    
    print("Bem-vindo ao TaskTracker!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            atualizar_tarefa(tarefas)
        elif opcao == "5":
            print("\nEncerrando o TaskTracker. Até a próxima!")
            break
        else:
            print("\n[ERRO] Opção inválida! Por favor, escolha um número entre 1 e 5.")


if __name__ == "__main__":
    main()