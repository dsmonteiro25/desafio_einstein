def calcular_fitness(individuo):
    """Avalia o indivíduo com base nas 15 regras do desafio."""
    pontos = 0
    
    # Mapear casas por atributo para fácil acesso
    casas_por_cor = {casa["cor"]: casa for casa in individuo}
    casas_por_nacionalidade = {casa["nacionalidade"]: casa for casa in individuo}
    casas_por_cigarro = {casa["cigarro"]: casa for casa in individuo}
    
    # Regra 1: O Norueguês vive na primeira casa
    if individuo[0]["nacionalidade"] == "Norueguês":
        pontos += 1
    
    # Regra 2: O Inglês vive na casa Vermelha
    casa_ingles = casas_por_nacionalidade.get("Inglês")
    if casa_ingles and casa_ingles["cor"] == "Vermelha":
        pontos += 1
    
    # Regra 3: O Sueco tem Cachorros
    casa_sueco = casas_por_nacionalidade.get("Sueco")
    if casa_sueco and casa_sueco["animal"] == "Cachorros":
        pontos += 1
    
    # Regra 4: O Dinamarquês bebe Chá
    casa_dinamarques = casas_por_nacionalidade.get("Dinamarquês")
    if casa_dinamarques and casa_dinamarques["bebida"] == "Chá":
        pontos += 1
    
    # Regra 5: Casa Verde imediatamente à esquerda da Branca
    try:
        indice_verde = next(i for i, casa in enumerate(individuo) if casa["cor"] == "Verde")
        indice_branca = next(i for i, casa in enumerate(individuo) if casa["cor"] == "Branca")
        if indice_verde + 1 == indice_branca:
            pontos += 1
    except StopIteration:
        pass
    
    # Regra 6: Casa Verde bebe Café
    casa_verde = casas_por_cor.get("Verde")
    if casa_verde and casa_verde["bebida"] == "Café":
        pontos += 1
    
    # Regra 7: Fumante de Pall Mall cria Pássaros
    casa_pallmall = casas_por_cigarro.get("Pall Mall")
    if casa_pallmall and casa_pallmall["animal"] == "Pássaros":
        pontos += 1
    
    # Regra 8: Casa Amarela fuma Dunhill
    casa_amarela = casas_por_cor.get("Amarela")
    if casa_amarela and casa_amarela["cigarro"] == "Dunhill":
        pontos += 1
    
    # Regra 9: Casa do meio bebe Leite
    if individuo[2]["bebida"] == "Leite":
        pontos += 1
    
    # Regra 10: Fumante de Blends ao lado de quem tem Gatos
    for i, casa in enumerate(individuo):
        if casa["cigarro"] == "Blends":
            vizinhos = []
            if i > 0: vizinhos.append(individuo[i-1])
            if i < 4: vizinhos.append(individuo[i+1])
            if any(viz["animal"] == "Gatos" for viz in vizinhos):
                pontos += 1
                break
    
    # Regra 11: Dono de Cavalos ao lado de quem fuma Dunhill
    for i, casa in enumerate(individuo):
        if casa["animal"] == "Cavalos":
            vizinhos = []
            if i > 0: vizinhos.append(individuo[i-1])
            if i < 4: vizinhos.append(individuo[i+1])
            if any(viz["cigarro"] == "Dunhill" for viz in vizinhos):
                pontos += 1
                break
    
    # Regra 12: Fumante de BlueMaster bebe Cerveja
    casa_bluemaster = casas_por_cigarro.get("BlueMaster")
    if casa_bluemaster and casa_bluemaster["bebida"] == "Cerveja":
        pontos += 1
    
    # Regra 13: Alemão fuma Prince
    casa_alemao = casas_por_nacionalidade.get("Alemão")
    if casa_alemao and casa_alemao["cigarro"] == "Prince":
        pontos += 1
    
    # Regra 14: Norueguês ao lado da casa Azul
    casa_noruegues = casas_por_nacionalidade.get("Norueguês")
    if casa_noruegues:
        indice = individuo.index(casa_noruegues)
        if (indice > 0 and individuo[indice-1]["cor"] == "Azul") or \
           (indice < 4 and individuo[indice+1]["cor"] == "Azul"):
            pontos += 1
    
    # Regra 15: Fumante de Blends vizinho de quem bebe Água
    for i, casa in enumerate(individuo):
        if casa["cigarro"] == "Blends":
            vizinhos = []
            if i > 0: vizinhos.append(individuo[i-1])
            if i < 4: vizinhos.append(individuo[i+1])
            if any(viz["bebida"] == "Água" for viz in vizinhos):
                pontos += 1
                break
    
    return pontos