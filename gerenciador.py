def adcionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append({'tarefa': tarefa, 'completa': False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    return


def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa['completa'] else " "
        print(f"{indice}. [{status}] - {tarefa['tarefa']}")
    return    
        
        
def atualizar_nome_tarefa(tarefas, indice, novo_nome_tarefa):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]['tarefa'] = novo_nome_tarefa
        print(f"Atualizando tarefa {indice} para '{novo_nome_tarefa}'")
    else:
        print("Índice inválido. Tarefa não encontrada.")
        
    return


def completar_tarefa(tarefas, indice):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]['completa'] = True
        print(f"Tarefa {indice} marcada como completa.")
    else:
        print("Índice inválido. Tarefa não encontrada.")
        
    return


def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa['completa']:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas com sucesso!")
    return


tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    
    opcao = input("Digite a sua escolha: ")
    
    if opcao == '1':
        adcionar_tarefa(tarefas)    
    elif opcao == '2':
        ver_tarefas(tarefas)
    elif opcao == '3':
        ver_tarefas(tarefas)
        indice = int(input("Digite o índice da tarefa a ser atualizada: "))
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice, novo_nome_tarefa)
    elif opcao == '4':
        ver_tarefas(tarefas)
        indice = int(input("Digite o índice da tarefa a ser marcada como completa: "))
        completar_tarefa(tarefas, indice)
    elif opcao == '5':
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    if opcao == '6':
        break
    
print("Programa encerrado. Até logo!")