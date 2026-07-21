from src.models.problem_model import PermutationProblem
import numpy as np

class TwoPhaseSolver:
    """
    Estrutura base para um resolvedor de duas fases inspirado no Cubo Mágico.
    """
    def __init__(self, problem: PermutationProblem):
        self.problem = problem
        self.current_state = problem.get_initial_state()

    def solve(self):
        print("Iniciando resolvedor de duas fases...")
        # Fase 1: Redução ao subgrupo G1-análogo
        self._phase1()
        print("Fase 1 concluída. Estado intermediário:", self.current_state)

        # Fase 2: Resolução final dentro do subgrupo
        self._phase2()
        print("Fase 2 concluída. Estado final:", self.current_state)
        print(f"Custo final: {self.problem.get_cost(self.current_state)}")
        return self.current_state

    def _phase1(self):
        """
        Implementação da Fase 1: Levar o problema para um estado do subgrupo G1-análogo.
        Esta é uma versão simplificada/placeholder.
        """
        print("Executando Fase 1: Redução ao subgrupo...")
        # Lógica de busca para atingir o estado do subgrupo
        # Exemplo: realizar alguns movimentos aleatórios para simular a busca
        for _ in range(5):
            if isinstance(self.problem, PermutationProblem):
                move = self.problem.get_random_move() if hasattr(self.problem, 'get_random_move') else (0,1)
                self.current_state = self.problem.apply_move(self.current_state, move)
            print(f"  Movimento na Fase 1. Estado atual: {self.current_state}")
        # Aqui, o estado deveria satisfazer as propriedades do subgrupo

    def _phase2(self):
        """
        Implementação da Fase 2: Resolver o problema dentro do subgrupo.
        Esta é uma versão simplificada/placeholder.
        """
        print("Executando Fase 2: Resolução dentro do subgrupo...")
        # Lógica de busca para resolver o problema a partir do estado do subgrupo
        # Exemplo: realizar mais alguns movimentos aleatórios
        for _ in range(3):
            if isinstance(self.problem, PermutationProblem):
                move = self.problem.get_random_move() if hasattr(self.problem, 'get_random_move') else (0,1)
                self.current_state = self.problem.apply_move(self.current_state, move)
            print(f"  Movimento na Fase 2. Estado atual: {self.current_state}")
        # Aqui, o estado deveria ser a solução otimizada

if __name__ == "__main__":
    # Exemplo de uso com o problema TSP
    from src.models.problem_model import TSPProblem

    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    tsp_problem = TSPProblem(distances)
    solver = TwoPhaseSolver(tsp_problem)
    final_state = solver.solve()
    print(f"\nEstado final após resolução: {final_state}")
    print(f"Custo do estado final: {tsp_problem.get_cost(final_state)}")
