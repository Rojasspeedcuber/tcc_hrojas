import numpy as np

def two_opt_swap(route, i, k):
    """
    Realiza uma operação 2-opt swap na rota.
    Troca os segmentos entre i e k.
    """
    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
    return new_route

def two_opt(problem, initial_route, max_iterations=1000):
    """
    Implementa o algoritmo 2-opt para otimização de rotas TSP.
    """
    best_route = list(initial_route)
    best_cost = problem.get_cost(best_route)
    improved = True
    iterations = 0

    while improved and iterations < max_iterations:
        improved = False
        for i in range(1, len(best_route) - 1):
            for k in range(i + 1, len(best_route)):
                new_route = two_opt_swap(best_route, i, k)
                new_cost = problem.get_cost(new_route)

                if new_cost < best_cost:
                    best_route = new_route
                    best_cost = new_cost
                    improved = True
        iterations += 1

    return best_route, best_cost

if __name__ == "__main__":
    from src.models.problem_model import TSPProblem
    
    # Exemplo de uso com o problema TSP
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    cities_coords = np.array([
        [0,0], [0,10], [10,0], [10,10]
    ])
    tsp_problem = TSPProblem(cities_coords, distances)
    
    initial_route = [0, 1, 2, 3] # Exemplo de rota inicial
    initial_cost = tsp_problem.get_cost(initial_route)
    print(f"Rota inicial: {initial_route}, Custo: {initial_cost}")

    optimized_route, optimized_cost = two_opt(tsp_problem, initial_route)
    print(f"Rota otimizada (2-opt): {optimized_route}, Custo: {optimized_cost}")
