def mochilavalor(solucao, valores):
    """Calcula o valor total da mochila dada uma solução."""
    return sum(solucao[i] * valores[i] for i in range(len(solucao)))

def mochila_peso(solucao, pesos):
    """Calcula o peso total da mochila dada uma solução."""
    return sum(solucao[i] * pesos[i] for i in range(len(solucao)))
