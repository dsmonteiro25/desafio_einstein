from algoritmo_genetico import criar_populacao, evolucionar
from fitness import calcular_fitness
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
    inicio = time.time()
    geracoes_sem_melhoria = 0
    
    # Execução do AG
    for geracao in range(GERACOES_MAX):
        populacao, fitness_atual = evolucionar(populacao, TAXA_MUTACAO, ELITE_SIZE)
        
        # Atualizar melhor solução encontrada
        if fitness_atual > melhor_fitness:
            melhor_fitness = fitness_atual
            melhor_individuo = next(ind for ind in populacao if calcular_fitness(ind) == melhor_fitness)
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
        regras = [
            "1. Norueguês na primeira casa",
            "2. Inglês na casa Vermelha",
            "3. Sueco tem Cachorros",
            "4. Dinamarquês bebe Chá",
            "5. Verde à esquerda da Branca",
            "6. Casa Verde bebe Café",
            "7. Pall Mall cria Pássaros",
            "8. Casa Amarela fuma Dunhill",
            "9. Casa do meio bebe Leite",
            "10. Blends ao lado de Gatos",
            "11. Cavalos ao lado de Dunhill",
            "12. BlueMaster bebe Cerveja",
            "13. Alemão fuma Prince",
            "14. Norueguês ao lado da Azul",
            "15. Blends vizinho de Água"
        ]
        fitness = calcular_fitness(melhor_individuo)
        for i in range(15):
            print(f"{regras[i]}: {'✓' if (fitness >> i) & 1 else '✗'}")

if __name__ == "__main__":
    executar_algoritmo_genetico()