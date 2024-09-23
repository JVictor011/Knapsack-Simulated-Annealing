# Knapsack-Simulated-Annealing

## Descrição do Projeto

Este projeto implementa o algoritmo Simulated Annealing para solucionar o problema da mochila ou outro problema de otimização à sua escolha. O problema da mochila consiste em selecionar itens com diferentes pesos e valores de forma a maximizar o valor total sem exceder a capacidade máxima da mochila.

## Problema da Mochila

Criar uma instância com pelo menos 20 itens, com pesos entre 1 a 50 kg e valores de importância entre 1 a 100 unidades. A mochila deve ter capacidade máxima de 500 kg.

## Problema Resolvido em Pesquisa Operacional

**Variáveis**:
\[
X_i = \begin{cases} 
1, & \text{se o item } i \text{ foi escolhido} \\ 
0, & \text{caso contrário}
\end{cases}
\quad \forall i = \{1, 2, \dots, 50\}
\]

**Modelo**:

\[
\text{max} \sum_{i=1}^{50} v_i X_i
\]

Sujeito a:

\[
\sum_{i=1}^{50} p_i X_i \leq 500
\]

\[
X_i \in \{0, 1\}
\]

## Requisitos

- Python 3.x
- Bibliotecas necessárias 
- [matplotlib](https://pypi.org/project/matplotlib/)

## Pseudo Algoritmo

O algoritmo Simulated Annealing segue o seguinte pseudo código:

1. Inicializar a solução atual com uma solução aleatória.
2. Definir a temperatura inicial.
3. Enquanto a temperatura não atingir o valor mínimo:
   1. Gerar uma nova solução vizinha.
   2. Calcular a diferença de valor entre a nova solução e a solução atual.
   3. Se a nova solução for melhor, aceitar a nova solução.
   4. Se a nova solução for pior, aceitar a nova solução com uma probabilidade que depende da temperatura e da diferença de valor.
   5. Reduzir a temperatura.
4. Retornar a melhor solução encontrada.


## Estrutura do Projeto

A implementação do algoritmo está dividida em diferentes módulos:

- `main.py`: Ponto de entrada do programa, executa o algoritmo e exibe os resultados.
- `presentation/cli.py`: Interface de linha de comando para executar o algoritmo.
- `use_cases/simulated_annealing.py`: Implementação do algoritmo Simulated Annealing.
- `domain/knapsack.py`: Funções para calcular o peso e valor da mochila.

## Exemplo de Execução

Para executar o algoritmo, utilize o comando:

```bash
python main.py
```

## Comparação com o Valor Ótimo

Para comparar o resultado obtido com o valor ótimo, você deve implementar o modelo matemático do problema da mochila e executar a instância criada. As funções `mochila_valor` e `mochila_peso` em `domain/knapsack.py` podem ser utilizadas para calcular o valor e peso da solução.

## Referências

- [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Problema da Mochila](https://pt.wikipedia.org/wiki/Problema_da_mochila)

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novas funcionalidades para este projeto. Faça um fork do repositório e envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
