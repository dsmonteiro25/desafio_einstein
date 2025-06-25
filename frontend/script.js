document.addEventListener('DOMContentLoaded', () => {
    let fitnessChart;
    const ctx = document.getElementById('fitnessChart').getContext('2d');

    function inicializarGrafico() {
        fitnessChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Melhor Fitness por Geração',
                    data: [],
                    borderColor: '#2563eb',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    tension: 0.2,
                    fill: true,
                    pointRadius: 3
                }]
            },
            options: {
                responsive: true,
                animation: false,
                scales: {
                    y: { beginAtZero: true, max: 15 },
                    x: { title: { display: true, text: 'Geração' } }
                }
            }
        });
    }

    const tableBody = document.getElementById('solution-table-body');
    const solutionFitnessSpan = document.getElementById('solution-fitness');
    const runSimulationBtn = document.getElementById('runSimulationBtn');
    const simulationMessage = document.getElementById('simulationMessage');

    function displaySolution(solution, fitness) {
        tableBody.innerHTML = '';
        solution.forEach((casa, index) => {
            const row = document.createElement('tr');
            row.className = (index % 2 === 0) ? 'row-even' : 'row-odd';
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

    // Evento do botão para chamar a API
    runSimulationBtn.addEventListener('click', () => {
        const popSize = parseInt(document.getElementById('popSize').value);
        const maxGenerations = parseInt(document.getElementById('maxGenerations').value);
        const mutationRate = parseFloat(document.getElementById('mutationRate').value) / 100;
        const eliteSize = parseFloat(document.getElementById('eliteSize').value) / 100;

        simulationMessage.innerHTML = `<p>Executando simulação... aguarde!</p>`;
        simulationMessage.style.display = 'block';

        fetch("http://localhost:5000/executar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                populacao: popSize,
                geracoes: maxGenerations,
                mutacao: mutationRate,
                elitismo: eliteSize
            })
        })
        .then(response => {
            if (!response.ok) throw new Error("Erro na resposta da API");
            return response.json();
        })
        .then(data => {
            if (fitnessChart) {
                fitnessChart.data.labels = [];
                fitnessChart.data.datasets[0].data = [];
                fitnessChart.update();
            } else {
                inicializarGrafico();
            }

            fitnessChart.data.labels = data.historico.map((_, i) => i + 1);
            fitnessChart.data.datasets[0].data = data.historico;
            fitnessChart.update();


            displaySolution(data.solucao, data.fitness);
            simulationMessage.innerHTML = `<p>Solução gerada com fitness: <strong>${data.fitness}/15</strong></p>`;

            const logContent = document.getElementById('log-content');
            logContent.innerHTML = ''; // limpa execuções anteriores

            if (data.log && data.log.length > 0) {
                logContent.innerHTML = data.log.join('\n');
            }

        })
        .catch(err => {
            console.error(err);
            simulationMessage.innerHTML = `<p style="color:red;">Erro ao conectar com a API.</p>`;
        });
    });
});
