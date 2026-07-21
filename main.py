import numpy as np
import os
import json
from src.data.instance_generator import generate_tsp_instance, save_tsp_instance
from src.models.problem_model import TSPProblem
from src.algorithms.two_phase_solver import TwoPhaseSolver
import time

def run_experiment(num_cities, num_clusters, seed=42):
    print(f"--- Experimento: {num_cities} cidades, {num_clusters} clusters ---")
    
    # 1. Gerar ou carregar instância
    cities_coords, distances = generate_tsp_instance(num_cities, seed=seed)
    save_tsp_instance(f"tsp_{num_cities}_cities.json", cities_coords, distances)
    
    problem = TSPProblem(cities_coords, distances)
    
    # 2. Executar resolvedor de duas fases
    solver = TwoPhaseSolver(problem, num_clusters=num_clusters)
    
    start_time = time.time()
    final_route = solver.solve(seed=seed)
    end_time = time.time()
    
    # 3. Exibir resultados
    duration = end_time - start_time
    final_cost = problem.get_cost(final_route)
    
    print(f"\nResultados:")
    print(f"Tempo de execução: {duration:.4f}s")
    print(f"Custo final: {final_cost:.2f}")
    
    # Salvar resultados
    results = {
        "num_cities": num_cities,
        "num_clusters": num_clusters,
        "seed": seed,
        "duration": duration,
        "final_cost": final_cost,
        "route": [int(i) for i in final_route]
    }
    
    results_path = os.path.join("data", "results", f"results_{num_cities}_c{num_clusters}.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Resultados salvos em: {results_path}\n")

if __name__ == "__main__":
    # Criar diretórios se não existirem
    os.makedirs("data/instances", exist_ok=True)
    os.makedirs("data/results", exist_ok=True)
    
    # Rodar alguns experimentos de teste
    run_experiment(num_cities=20, num_clusters=4)
    run_experiment(num_cities=50, num_clusters=6)
    run_experiment(num_cities=100, num_clusters=10)
