from use_cases.simulated_annealing import simulated_annealing
from domain.knapsack import mochila_peso
import random

def run_knapsack():
    """Executa o algoritmo e exibe os resultados."""
    valores = [random.randint(1, 100) for _ in range(20)]
    pesos = [random.randint(1, 50) for _ in range(20)]
    capacidade = 500

    melhor_solucao, melhor_valor = simulated_annealing(valores, pesos, capacidade)

    print("Melhor solução encontrada:", melhor_solucao)
    print("Valor da melhor solução:", melhor_valor)
    print("Peso da melhor solução:", mochila_peso(melhor_solucao, pesos))
