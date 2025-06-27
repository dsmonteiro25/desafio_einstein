def calcular_fitness(individuo):
    pontos = 0
    regras_atendidas = [False] * 15
    
    # Mapear casas por atributo para fácil acesso
    casas_por_cor = {casa["cor"]: casa for casa in individuo}
    casas_por_nacionalidade = {casa["nacionalidade"]: casa for casa in individuo}
    casas_por_cigarro = {casa["cigarro"]: casa for casa in individuo}
    casas_por_bebida = {casa["bebida"]: casa for casa in individuo}
    casas_por_animal = {casa["animal"]: casa for casa in individuo}
    
    # Regra 1: O Norueguês vive na primeira casa
    if individuo[0]["nacionalidade"] == "Norueguês":
        pontos += 1
        regras_atendidas[0] = True
    
    # Regra 2: O Inglês vive na casa Vermelha
    casa_ingles = casas_por_nacionalidade.get("Inglês")
    if casa_ingles and casa_ingles["cor"] == "Vermelha":
        pontos += 1
        regras_atendidas[1] = True
    
    # Regra 3: O Sueco tem Cachorros
    casa_sueco = casas_por_nacionalidade.get("Sueco")
    if casa_sueco and casa_sueco["animal"] == "Cachorros":
        pontos += 1
        regras_atendidas[2] = True
    
    # Regra 4: O Dinamarquês bebe Chá
    casa_dinamarques = casas_por_nacionalidade.get("Dinamarquês")
    if casa_dinamarques and casa_dinamarques["bebida"] == "Chá":
        pontos += 1
        regras_atendidas[3] = True
    
    # Regra 5: A casa Verde fica do lado esquerdo da casa Branca
    try:
        indice_branca = [i for i, casa in enumerate(individuo) if casa["cor"] == "Branca"][0]
        if indice_branca > 0 and individuo[indice_branca - 1]["cor"] == "Verde":
            pontos += 1
            regras_atendidas[4] = True
    except IndexError:
        pass
    
    # Regra 6: O homem que vive na casa Verde bebe Café
    casa_verde = casas_por_cor.get("Verde")
    if casa_verde and casa_verde["bebida"] == "Café":
        pontos += 1
        regras_atendidas[5] = True
        
    # Regra 7: O homem que fuma Pall Mall cria Pássaros
    casa_pall_mall = casas_por_cigarro.get("Pall Mall")
    if casa_pall_mall and casa_pall_mall["animal"] == "Pássaros":
        pontos += 1
        regras_atendidas[6] = True
        
    # Regra 8: O homem que vive na casa Amarela fuma Dunhill
    casa_amarela = casas_por_cor.get("Amarela")
    if casa_amarela and casa_amarela["cigarro"] == "Dunhill":
        pontos += 1
        regras_atendidas[7] = True
        
    # Regra 9: O homem que vive na casa do meio (posição 2, índice 2) bebe Leite
    if individuo[2]["bebida"] == "Leite":
        pontos += 1
        regras_atendidas[8] = True
        
    # Regra 10: O homem que fuma Blends vive ao lado do que tem Gatos
    casa_blends = casas_por_cigarro.get("Blends")
    casa_gatos = casas_por_animal.get("Gatos")
    if casa_blends and casa_gatos:
        indice_blends = individuo.index(casa_blends)
        indice_gatos = individuo.index(casa_gatos)
        if abs(indice_blends - indice_gatos) == 1:
            pontos += 1
            regras_atendidas[9] = True
            
    # Regra 11: O homem que cria Cavalos vive ao lado do que fuma Dunhill
    casa_cavalos = casas_por_animal.get("Cavalos")
    casa_dunhill = casas_por_cigarro.get("Dunhill")
    if casa_cavalos and casa_dunhill:
        indice_cavalos = individuo.index(casa_cavalos)
        indice_dunhill = individuo.index(casa_dunhill)
        if abs(indice_cavalos - indice_dunhill) == 1:
            pontos += 1
            regras_atendidas[10] = True
            
    # Regra 12: O homem que fuma BlueMaster bebe Cerveja
    casa_bluemaster = casas_por_cigarro.get("BlueMaster")
    if casa_bluemaster and casa_bluemaster["bebida"] == "Cerveja":
        pontos += 1
        regras_atendidas[11] = True
    
    # Regra 13: O Alemão fuma Prince
    casa_alemao = casas_por_nacionalidade.get("Alemão")
    if casa_alemao and casa_alemao["cigarro"] == "Prince":
        pontos += 1
        regras_atendidas[12] = True
    
    # Regra 14: O Norueguês vive ao lado da casa Azul
    casa_noruegues = casas_por_nacionalidade.get("Norueguês")
    casa_azul = casas_por_cor.get("Azul")
    if casa_noruegues and casa_azul:
        indice_noruegues = individuo.index(casa_noruegues)
        indice_azul = individuo.index(casa_azul)
        if abs(indice_noruegues - indice_azul) == 1:
            pontos += 1
            regras_atendidas[13] = True
    
    # Regra 15: O homem que fuma Blends é vizinho do que bebe Água
    casa_blends = casas_por_cigarro.get("Blends")
    casa_agua = casas_por_bebida.get("Água")
    if casa_blends and casa_agua:
        indice_blends = individuo.index(casa_blends)
        indice_agua = individuo.index(casa_agua)
        if abs(indice_blends - indice_agua) == 1:
            pontos += 1
            regras_atendidas[14] = True
    
    return pontos, regras_atendidas