import os as o

def lista_tarefas():

    equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
    equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}
    tarefas_combinadas = equipe_a.union(equipe_b)

    print('Tarefas Combinadas:')
    print(f'{tarefas_combinadas}')
    tarefa_remover = input("Digite a tarefa a ser removida: ").lower()

    if tarefa_remover in tarefas_combinadas:

       tarefas_combinadas.remove(tarefa_remover)

    print(f"Tarefas finais: {tarefas_combinadas}")

if __name__=='__main__':
    o.system('cls' if o.name == 'nt' else 'clear')
    lista_tarefas()