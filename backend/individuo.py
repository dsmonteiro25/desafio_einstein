import random

# Domínios possíveis para cada atributo
CORES = ["Amarela", "Azul", "Branca", "Verde", "Vermelha"]
NACIONALIDADES = ["Norueguês", "Inglês", "Sueco", "Dinamarquês", "Alemão"]
BEBIDAS = ["Água", "Café", "Cerveja", "Chá", "Leite"]
CIGARROS = ["Blends", "BlueMaster", "Dunhill", "Pall Mall", "Prince"]
ANIMAIS = ["Cachorros", "Cavalos", "Gatos", "Pássaros", "Peixes"]

def criar_individuo_valido():
    """Gera indivíduos garantindo que cada atributo aparece exatamente uma vez"""
    individuo = []
    atributos = {
        "cor": random.sample(CORES, len(CORES)),
        "nacionalidade": random.sample(NACIONALIDADES, len(NACIONALIDADES)),
        "bebida": random.sample(BEBIDAS, len(BEBIDAS)),
        "cigarro": random.sample(CIGARROS, len(CIGARROS)),
        "animal": random.sample(ANIMAIS, len(ANIMAIS))
    }
    
    for i in range(5):
        casa = {
            "cor": atributos["cor"][i],
            "nacionalidade": atributos["nacionalidade"][i],
            "bebida": atributos["bebida"][i],
            "cigarro": atributos["cigarro"][i],
            "animal": atributos["animal"][i]
        }
        individuo.append(casa)
    return individuo

def corrigir_duplicatas(individuo):
    """Corrige atributos duplicados mantendo a validade do indivíduo"""
    for atributo in ["cor", "nacionalidade", "bebida", "cigarro", "animal"]:
        valores = [casa[atributo] for casa in individuo]
        if len(set(valores)) != 5:  # Há duplicatas
            dominio = globals()[atributo.upper()]
            disponiveis = [v for v in dominio if v not in valores]
            for i, casa in enumerate(individuo):
                if valores.count(casa[atributo]) > 1:
                    if disponiveis:
                        casa[atributo] = disponiveis.pop()
                    else:
                        # Se não houver valores disponíveis, troca com outra casa
                        for j in range(5):
                            if valores.count(individuo[j][atributo]) == 1:
                                individuo[i][atributo], individuo[j][atributo] = individuo[j][atributo], individuo[i][atributo]
                                break
    return individuo