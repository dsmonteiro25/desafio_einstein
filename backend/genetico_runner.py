from algoritmo_genetico import criar_populacao, evolucionar
from fitness import calcular_fitness

def executar_algoritmo(pop_size=500, max_geracoes=2000, taxa_mutacao=0.15, elite_size=0.15):
    populacao = criar_populacao(pop_size)
    melhor_fitness = 0
    melhor_individuo = None
    historico_fitness = []

    for _ in range(max_geracoes):
        populacao, _ = evolucionar(populacao, taxa_mutacao, elite_size)

        for ind in populacao:
            fit, _ = calcular_fitness(ind)
            if fit > melhor_fitness:
                melhor_fitness = fit
                melhor_individuo = ind

        historico_fitness.append(melhor_fitness)

        if melhor_fitness == 15:
            break

    return {
        "fitness": melhor_fitness,
        "solucao": melhor_individuo,
        "historico": historico_fitness
    }
