import random
from individuo import criar_individuo_valido, corrigir_duplicatas
from fitness import calcular_fitness

def selecionar_por_torneio(populacao, fitness_populacao, tamanho_torneio=3):
    """Seleção por torneio com tamanho ajustável"""
    participantes = random.sample(list(zip(populacao, fitness_populacao)), tamanho_torneio)
    return max(participantes, key=lambda x: x[1])[0]

def crossover_ordenado(pai1, pai2):
    """Crossover que preserva a unicidade dos atributos"""
    ponto_corte = random.randint(1, 3)
    filho1 = pai1[:ponto_corte]
    
    # Adicionar genes do pai2 mantendo a unicidade
    for casa in pai2:
        if all(casa["nacionalidade"] != f["nacionalidade"] for f in filho1):
            filho1.append(casa)
    
    # Completar com genes aleatórios se necessário
    while len(filho1) < 5:
        novo_individuo = criar_individuo_valido()
        for casa in novo_individuo:
            if all(casa["nacionalidade"] != f["nacionalidade"] for f in filho1):
                filho1.append(casa)
                if len(filho1) == 5:
                    break
    
    # Garantir que todos os atributos são únicos
    filho1 = corrigir_duplicatas(filho1[:5])
    filho2 = pai2  # Simplificado para exemplo
    
    return filho1, filho2

def mutar_swap(individuo):
    """Troca dois atributos do mesmo tipo entre casas"""
    i, j = random.sample(range(5), 2)
    atributo = random.choice(["cor", "nacionalidade", "bebida", "cigarro", "animal"])
    individuo[i][atributo], individuo[j][atributo] = individuo[j][atributo], individuo[i][atributo]
    return individuo

def criar_populacao(tamanho):
    """Gera uma população inicial de indivíduos válidos."""
    return [criar_individuo_valido() for _ in range(tamanho)]

def evolucionar(populacao, taxa_mutacao=0.15, elite_size=0.15):
    """Executa uma geração do algoritmo genético."""
    fitness_populacao = [calcular_fitness(ind) for ind in populacao]
    nova_populacao = []
    
    # Elitismo: manter os melhores indivíduos
    elite = sorted(zip(populacao, fitness_populacao), key=lambda x: x[1], reverse=True)
    elite = [ind for ind, fit in elite[:int(len(populacao)*elite_size)]]
    nova_populacao.extend(elite)
    
    # Preencher o resto da população
    while len(nova_populacao) < len(populacao):
        try:
            # Seleção por torneio
            pai1 = selecionar_por_torneio(populacao, fitness_populacao)
            pai2 = selecionar_por_torneio(populacao, fitness_populacao)
            
            # Crossover
            filho1, filho2 = crossover_ordenado(pai1, pai2)
            
            # Mutação
            if random.random() < taxa_mutacao:
                filho1 = mutar_swap(filho1)
            if random.random() < taxa_mutacao:
                filho2 = mutar_swap(filho2)
            
            nova_populacao.extend([filho1, filho2])
        except Exception as e:
            # Em caso de erro, adicionar novos indivíduos válidos
            nova_populacao.extend([criar_individuo_valido(), criar_individuo_valido()])
    
    return nova_populacao[:len(populacao)], max(fitness_populacao)