document.addEventListener('DOMContentLoaded', () => {
    const tableBody = document.getElementById('solution-table-body');
    const solutionFitnessSpan = document.getElementById('solution-fitness');
    const runSimulationBtn = document.getElementById('runSimulationBtn');
    const simulationMessage = document.getElementById('simulationMessage');

    // Dados da solução de exemplo (baseado na sua última saída com 12/15 de fitness)
    const exampleSolution = [
        { "cor": "Azul", "nacionalidade": "Alemão", "bebida": "Café", "cigarro": "Pall Mall", "animal": "Peixes" },
        { "cor": "Branca", "nacionalidade": "Inglês", "bebida": "Leite", "cigarro": "Prince", "animal": "Pássaros" },
        { "cor": "Verde", "nacionalidade": "Sueco", "bebida": "Água", "cigarro": "Blends", "animal": "Cachorros" },
        { "cor": "Amarela", "nacionalidade": "Dinamarquês", "bebida": "Chá", "cigarro": "Dunhill", "animal": "Gatos" },
        { "cor": "Vermelha", "nacionalidade": "Norueguês", "bebida": "Cerveja", "cigarro": "BlueMaster", "animal": "Cavalos" }
    ];

    const exampleFitness = 12; // Fitness da solução de exemplo

    // Função para preencher a tabela com uma solução
    function displaySolution(solution, fitness) {
        tableBody.innerHTML = ''; // Limpa a tabela existente
        solution.forEach((casa, index) => {
            const row = document.createElement('tr');
            row.className = (index % 2 === 0) ? 'row-even' : 'row-odd'; // Estilo zebrado
            row.innerHTML = `
                <td class="table-cell font-medium rounded-bl-lg">${index + 1}</td>
                <td class="table-cell">${casa.cor}</td>
                <td class="table-cell">${casa.nacionalidade}</td>
                <td class="table-cell">${casa.bebida}</td>
                <td class="table-cell">${casa.cigarro}</td>
                <td class="table-cell rounded-br-lg">${casa.animal}</td>
            `;
            tableBody.appendChild(row);
        });
        solutionFitnessSpan.textContent = `${fitness}/15`;
    }

    // Exibe a solução de exemplo ao carregar a página
    displaySolution(exampleSolution, exampleFitness);

    // Evento de clique do botão "Simular com Parâmetros"
    runSimulationBtn.addEventListener('click', () => {
        // Obter os valores dos parâmetros
        const popSize = document.getElementById('popSize').value;
        const maxGenerations = document.getElementById('maxGenerations').value;
        // Converter a porcentagem de volta para decimal para consistência com o backend
        const mutationRate = parseFloat(document.getElementById('mutationRate').value) / 100;
        const eliteSize = parseFloat(document.getElementById('eliteSize').value) / 100;

        // Exibir uma mensagem de simulação (aqui você enviaria para o backend)
        simulationMessage.innerHTML = `
            <p>Simulando algoritmo genético com os seguintes parâmetros:</p>
            <ul>
                <li>Tamanho da População: ${popSize}</li>
                <li>Máximo de Gerações: ${maxGenerations}</li>
                <li>Taxa de Mutação: ${mutationRate.toFixed(2)}</li>
                <li>Tamanho do Elitismo: ${eliteSize.toFixed(2)}</li>
            </ul>
            <p class="note">
                (Em uma aplicação completa, esses parâmetros seriam enviados ao backend Python para executar o AG.
                A solução exibida abaixo ainda é um exemplo fixo.)
            </p>
        `;
        simulationMessage.style.display = 'block'; // Mostra a mensagem
    });
});
