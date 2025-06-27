import random
from individuo import criar_individuo_valido, corrigir_duplicatas
from fitness import calcular_fitness # Importa a função calcular_fitness

def selecionar_por_roleta(populacao, fitness_populacao):
    """Seleção por roleta."""
    total_fitness = sum(fitness_populacao)
    
    # Se o total_fitness for 0 (todos os indivíduos têm fitness 0),
    # selecione aleatoriamente para evitar divisão por zero.
    if total_fitness == 0:
        return random.choice(populacao)

    limite = random.uniform(0, total_fitness)
    acumulado = 0
    for i, fitness in enumerate(fitness_populacao):
        acumulado += fitness
        if acumulado >= limite:
            return populacao[i]
    # Em caso de erro de arredondamento, retornar o último indivíduo
    return populacao[-1]

def crossover_ordenado(pai1, pai2):
    """Crossover que preserva a unicidade dos atributos."""
    
    # Extrai os atributos de cada pai
    atributos_pai1 = {
        "cor": [c["cor"] for c in pai1],
        "nacionalidade": [c["nacionalidade"] for c in pai1],
        "bebida": [c["bebida"] for c in pai1],
        "cigarro": [c["cigarro"] for c in pai1],
        "animal": [c["animal"] for c in pai1],
    }
    
    atributos_pai2 = {
        "cor": [c["cor"] for c in pai2],
        "nacionalidade": [c["nacionalidade"] for c in pai2],
        "bebida": [c["bebida"] for c in pai2],
        "cigarro": [c["cigarro"] for c in pai2],
        "animal": [c["animal"] for c in pai2],
    }
    
    # Realiza o crossover em cada lista de atributos individualmente
    ponto_corte = random.randint(1, 4)
    
    filho1_atributos = {}
    filho2_atributos = {}
    
    for atributo in atributos_pai1.keys():
        # Crossover de um ponto
        parte1_f1 = atributos_pai1[atributo][:ponto_corte]
        parte2_f1 = [item for item in atributos_pai2[atributo] if item not in parte1_f1]
        filho1_atributos[atributo] = parte1_f1 + parte2_f1
        
        parte1_f2 = atributos_pai2[atributo][:ponto_corte]
        parte2_f2 = [item for item in atributos_pai1[atributo] if item not in parte1_f2]
        filho2_atributos[atributo] = parte1_f2 + parte2_f2
        
    # Recria os indivíduos a partir dos atributos gerados
    filho1 = []
    filho2 = []
    
    for i in range(5):
        casa1 = {
            "cor": filho1_atributos["cor"][i],
            "nacionalidade": filho1_atributos["nacionalidade"][i],
            "bebida": filho1_atributos["bebida"][i],
            "cigarro": filho1_atributos["cigarro"][i],
            "animal": filho1_atributos["animal"][i],
        }
        filho1.append(casa1)
        
        casa2 = {
            "cor": filho2_atributos["cor"][i],
            "nacionalidade": filho2_atributos["nacionalidade"][i],
            "bebida": filho2_atributos["bebida"][i],
            "cigarro": filho2_atributos["cigarro"][i],
            "animal": filho2_atributos["animal"][i],
        }
        filho2.append(casa2)
        
    return filho1, filho2

def mutar_swap(individuo):
    """Mutação que troca dois atributos de uma mesma categoria."""
    atributo_para_mutar = random.choice(["cor", "nacionalidade", "bebida", "cigarro", "animal"])
    
    # Obter os índices de duas casas aleatórias para a troca
    idx1, idx2 = random.sample(range(5), 2)
    
    # Trocar o atributo selecionado entre as duas casas
    individuo[idx1][atributo_para_mutar], individuo[idx2][atributo_para_mutar] = \
        individuo[idx2][atributo_para_mutar], individuo[idx1][atributo_para_mutar]
        
    return individuo

def criar_populacao(tamanho):
    """Gera uma população inicial de indivíduos válidos."""
    return [criar_individuo_valido() for _ in range(tamanho)]

def evolucionar(populacao, taxa_mutacao=0.15, elite_size=0.15):
    """Executa uma geração do algoritmo genético."""
    # Aqui, calculamos apenas o valor do fitness para a seleção
    fitness_populacao = [calcular_fitness(ind)[0] for ind in populacao] # Pegar apenas os pontos
    nova_populacao = []
    
    # Elitismo: manter os melhores indivíduos
    elite = sorted(zip(populacao, fitness_populacao), key=lambda x: x[1], reverse=True)
    elite = [ind for ind, fit in elite[:int(len(populacao)*elite_size)]]
    nova_populacao.extend(elite)
    
    # Preencher o resto da população
    while len(nova_populacao) < len(populacao):
        try:
            # Seleção por roleta
            pai1 = selecionar_por_roleta(populacao, fitness_populacao)
            pai2 = selecionar_por_roleta(populacao, fitness_populacao)
            
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