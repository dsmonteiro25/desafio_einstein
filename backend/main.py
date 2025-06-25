from algoritmo_genetico import criar_populacao, evolucionar
from fitness import calcular_fitness # Importa a função calcular_fitness
import time

def executar_algoritmo_genetico():
    # Parâmetros otimizados
    TAMANHO_POPULACAO = 500
    GERACOES_MAX = 2000
    TAXA_MUTACAO = 0.15
    ELITE_SIZE = 0.15
    
    print("Iniciando algoritmo genético para o Desafio de Einstein...")
    print(f"Configuração: População={TAMANHO_POPULACAO}, Gerações={GERACOES_MAX}")
    
    # Inicialização
    populacao = criar_populacao(TAMANHO_POPULACAO)
    melhor_fitness = 0
    melhor_individuo = None
    melhores_regras_atendidas = [] # Para armazenar o status das regras do melhor indivíduo
    
    inicio = time.time()
    geracoes_sem_melhoria = 0
    
    # Execução do AG
    for geracao in range(GERACOES_MAX):
        populacao, fitness_atual_pop = evolucionar(populacao, TAXA_MUTACAO, ELITE_SIZE)
        
        # Recalcular o fitness do melhor indivíduo na população atual para garantir a consistência
        # e obter o status das regras.
        # Precisamos iterar sobre a população para encontrar o indivíduo com o maior fitness.
        current_best_ind = None
        current_best_fit_val = 0
        current_best_rules_status = []

        for ind in populacao:
            fit_val, rules_status = calcular_fitness(ind)
            if fit_val > current_best_fit_val:
                current_best_fit_val = fit_val
                current_best_ind = ind
                current_best_rules_status = rules_status
        
        # Atualizar melhor solução encontrada de todas as gerações
        if current_best_fit_val > melhor_fitness:
            melhor_fitness = current_best_fit_val
            melhor_individuo = current_best_ind
            melhores_regras_atendidas = current_best_rules_status
            geracoes_sem_melhoria = 0
            print(f"Geração {geracao}: Fitness = {melhor_fitness}/15")
            
            # Mostrar detalhes quando encontrar uma solução melhor
            if melhor_fitness >= 13:
                print("\nMelhor solução atual:")
                for i, casa in enumerate(melhor_individuo):
                    print(f"Casa {i+1}: {casa['cor']} | {casa['nacionalidade']} | {casa['bebida']} | {casa['cigarro']} | {casa['animal']}")
                print()
        else:
            geracoes_sem_melhoria += 1
        
        # Critérios de parada
        if melhor_fitness == 15:
            print("\nSOLUÇÃO PERFEITA ENCONTRADA!")
            break
            
        if geracoes_sem_melhoria > 200 and melhor_fitness >= 13:
            print("\nEstagnação - interrompendo execução...")
            break
    
    # Resultados finais
    tempo_execucao = time.time() - inicio
    print(f"\nTempo de execução: {tempo_execucao:.2f} segundos")
    print(f"Melhor fitness alcançado: {melhor_fitness}/15")
    
    if melhor_individuo:
        print("\nMelhor solução encontrada:")
        for i, casa in enumerate(melhor_individuo):
            print(f"\nCasa {i+1}:")
            print(f"  Cor: {casa['cor']}")
            print(f"  Nacionalidade: {casa['nacionalidade']}")
            print(f"  Bebida: {casa['bebida']}")
            print(f"  Cigarro: {casa['cigarro']}")
            print(f"  Animal: {casa['animal']}")
        
        # Verificar quais regras foram atendidas
        print("\nRegras atendidas:")
        regras_desc = [
            "1. Norueguês vive na primeira casa",
            "2. O Inglês vive na casa Vermelha",
            "3. O Sueco tem Cachorros",
            "4. O Dinamarquês bebe Chá",
            "5. A casa Verde fica do lado esquerdo da casa Branca",
            "6. O homem que vive na casa Verde bebe Café",
            "7. O homem que fuma Pall Mall cria Pássaros",
            "8. O homem que vive na casa Amarela fuma Dunhill",
            "9. O homem que vive na casa do meio bebe Leite",
            "10. O homem que fuma Blends vive ao lado do que tem Gatos",
            "11. O homem que cria Cavalos vive ao lado do que fuma Dunhill",
            "12. O homem que fuma BlueMaster bebe Cerveja",
            "13. O Alemão fuma Prince",
            "14. O Norueguês vive ao lado da casa Azul",
            "15. O homem que fuma Blends é vizinho do que bebe Água"
        ]
        
        for i, atendida in enumerate(melhores_regras_atendidas):
            print(f"{regras_desc[i]}: {'✓' if atendida else '✗'}")
        
        print(f"Total de regras atendidas: {melhor_fitness}/15")

if __name__ == "__main__":
    executar_algoritmo_genetico()