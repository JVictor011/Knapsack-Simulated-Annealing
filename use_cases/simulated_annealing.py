import math
import random
import matplotlib.pyplot as plt
from domain.knapsack import mochilavalor, mochila_peso

def temperatura_inicial():
    """Define a temperatura inicial do algoritmo."""
    return 1000  # Temperatura inicial

def diminui_temperatura(T):
    """Diminui a temperatura em cada iteração."""
    return T * 0.99  # Aumenta a taxa de resfriamento

def gerar_vizinho(solucao):
    """Gera uma nova solução vizinha trocando um item aleatório."""
    vizinho = solucao[:]
    index = random.randint(0, len(solucao) - 1)
    vizinho[index] = 1 - vizinho[index]  # Troca entre 0 e 1
    return vizinho

def simulated_annealing(valores, pesos, capacidade):
    """Executa o algoritmo Simulated Annealing para o problema da mochila."""
    solucao_atual = [random.randint(0, 1) for _ in range(len(valores))]
    valor_atual = mochilavalor(solucao_atual, valores)
    peso_atual = mochila_peso(solucao_atual, pesos)

    melhor_solucao = solucao_atual[:]
    melhor_valor = valor_atual

    T = temperatura_inicial()
    temperaturas = []

    while T > 1:
        temperaturas.append(T)

        nova_solucao = gerar_vizinho(solucao_atual)
        novo_valor = mochilavalor(nova_solucao, valores)
        novo_peso = mochila_peso(nova_solucao, pesos)

        if novo_peso <= capacidade:
            delta_valor = novo_valor - valor_atual

            if delta_valor > 0 or random.random() < math.exp(delta_valor / T):
                solucao_atual = nova_solucao
                valor_atual = novo_valor
                peso_atual = novo_peso

                if valor_atual > melhor_valor:
                    melhor_solucao = solucao_atual[:]
                    melhor_valor = valor_atual

        T = diminui_temperatura(T)

    plt.plot(temperaturas)
    plt.title("Evolução da Temperatura no Simulated Annealing")
    plt.xlabel("Iterações")
    plt.ylabel("Temperatura")
    plt.show()

    return melhor_solucao, melhor_valor
