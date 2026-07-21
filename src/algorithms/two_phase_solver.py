from src.models.problem_model import TSPProblem
from src.algorithms.two_opt import two_opt
import numpy as np

class TwoPhaseSolver:
    """
    Resolvedor de duas fases para o TSP inspirado no Cubo Mágico.
    """
    def __init__(self, problem: TSPProblem, num_clusters=4):
        self.problem = problem
        self.num_clusters = num_clusters
        self.current_state = problem.get_initial_state()

    def solve(self, seed=None):
        print(f"Iniciando resolvedor de duas fases (Clusters: {self.num_clusters})...")
        
        # Fase 1: Redução ao subgrupo G1-análogo (Clustering)
        self._phase1(seed)
        print(f"Fase 1 concluída. Custo intermediário: {self.problem.get_cost(self.current_state):.2f}")

        # Fase 2: Resolução final dentro do subgrupo (Busca Local / 2-opt)
        self._phase2()
        print(f"Fase 2 concluída. Custo final: {self.problem.get_cost(self.current_state):.2f}")
        
        return self.current_state

    def _phase1(self, seed):
        """
        Fase 1: Aplica clustering para atingir o estado G1-análogo.
        """
        print("Executando Fase 1: Agrupamento geográfico e ordem inter-cluster...")
        self.current_state = self.problem.apply_clustering(self.num_clusters, seed)

    def _phase2(self):
        """
        Fase 2: Aplica otimização 2-opt na rota resultante da Fase 1.
        """
        print("Executando Fase 2: Otimização local (2-opt)...")
        self.current_state, _ = two_opt(self.problem, self.current_state)

if __name__ == "__main__":
    # Exemplo de teste integrado
    from src.data.instance_generator import generate_tsp_instance
    
    num_cities = 30
    cities_coords, distances = generate_tsp_instance(num_cities, seed=42)
    tsp_problem = TSPProblem(cities_coords, distances)
    
    solver = TwoPhaseSolver(tsp_problem, num_clusters=5)
    final_route = solver.solve(seed=42)
    
    print(f"\nMelhor rota encontrada: {final_route}")
    print(f"Custo total: {tsp_problem.get_cost(final_route):.2f}")
