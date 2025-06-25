from flask import Flask, request, jsonify
from flask_cors import CORS
from algoritmo_genetico import criar_populacao, evolucionar
from fitness import calcular_fitness
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Descrições das 15 regras para exibir no log
REGRAS_DESC = [
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

@app.route("/executar", methods=["POST"])
def executar():
    dados = request.get_json()
    pop_size = int(dados.get("populacao", 500))
    max_geracoes = int(dados.get("geracoes", 2000))
    taxa_mutacao = float(dados.get("mutacao", 0.15))
    elite_size = float(dados.get("elitismo", 0.15))

    populacao = criar_populacao(pop_size)
    melhor_fitness = 0
    melhor_individuo = None
    melhores_regras = []
    historico = []
    log = []

    inicio = datetime.now()

    for geracao in range(max_geracoes):
        populacao, _ = evolucionar(populacao, taxa_mutacao, elite_size)

        for ind in populacao:
            fit, regras = calcular_fitness(ind)
            if fit > melhor_fitness:
                melhor_fitness = fit
                melhor_individuo = ind
                melhores_regras = regras
                log.append(f"Geração {geracao + 1}: Fitness = {melhor_fitness}/15")

        historico.append(melhor_fitness)

        if melhor_fitness == 15:
            log.append("Solução perfeita encontrada!")
            break

    duracao = (datetime.now() - inicio).total_seconds()
    log.append(f"\nTempo de execução: {duracao:.2f} segundos")

    if melhor_individuo:
        log.append("\nMelhor solução encontrada:")
        for i, casa in enumerate(melhor_individuo):
            linha = f"Casa {i+1}: {casa['cor']} | {casa['nacionalidade']} | {casa['bebida']} | {casa['cigarro']} | {casa['animal']}"
            log.append(linha)

        log.append("\nRegras atendidas:")
        for i, status in enumerate(melhores_regras):
            simbolo = "V" if status else "X"
            log.append(f"{simbolo} {REGRAS_DESC[i]}")

        log.append(f"\nTotal de regras atendidas: {melhor_fitness}/15")

    return jsonify({
        "fitness": melhor_fitness,
        "solucao": melhor_individuo,
        "historico": historico,
        "log": log
    })

@app.route("/", methods=["GET"])
def home():
    return "<h2>API do Desafio de Einstein está online!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
