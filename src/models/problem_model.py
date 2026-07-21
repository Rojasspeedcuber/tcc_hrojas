import numpy as np

class PermutationProblem:
    """
    Classe base para modelar problemas de otimização de permutação.
    """
    def __init__(self, num_elements):
        self.num_elements = num_elements
        self.current_state = np.arange(num_elements) # Exemplo: permutação inicial

    def get_cost(self, permutation):
        """
        Calcula o custo de uma dada permutação. Deve ser implementado pelas subclasses.
        """\n        raise NotImplementedError("Método get_cost deve ser implementado.")

    def apply_move(self, state, move):
        """
        Aplica um 'movimento' ao estado atual, gerando um novo estado.
        Este método simularia as operações de permutação.
        """
        # Exemplo simplificado: troca de dois elementos
        new_state = state.copy()
        idx1, idx2 = move
        new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
        return new_state

    def get_initial_state(self):
        return self.current_state.copy()

    def is_goal_state(self, state):
        """
        Verifica se o estado atual é um estado objetivo (resolvido ou otimizado).
        """
        # Para problemas de otimização, isso geralmente significa que não há melhoria possível
        return False

class TSPProblem(PermutationProblem):
    """
    Exemplo de implementação para o Problema do Caixeiro Viajante (TSP).
    """
    def __init__(self, distances_matrix):
        super().__init__(len(distances_matrix))
        self.distances_matrix = distances_matrix

    def get_cost(self, permutation):
        cost = 0
        for i in range(self.num_elements - 1):
            cost += self.distances_matrix[permutation[i], permutation[i+1]]
        cost += self.distances_matrix[permutation[self.num_elements-1], permutation[0]] # Volta ao início
        return cost

    def get_random_move(self):
        # Exemplo de movimento: troca de duas cidades aleatórias
        idx1, idx2 = np.random.choice(self.num_elements, 2, replace=False)
        return (idx1, idx2)

if __name__ == "__main__":
    # Exemplo de uso
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    tsp = TSPProblem(distances)
    initial_permutation = tsp.get_initial_state()
    print(f"Permutação Inicial: {initial_permutation}, Custo: {tsp.get_cost(initial_permutation)}")

    # Aplicar um movimento (trocar 0 e 1)
    moved_permutation = tsp.apply_move(initial_permutation, (0, 1))
    print(f"Permutação Após Movimento (0,1): {moved_permutation}, Custo: {tsp.get_cost(moved_permutation)}")
