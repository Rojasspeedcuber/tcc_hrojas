import numpy as np
import json
import os

def generate_tsp_instance(num_cities, x_range=(0, 100), y_range=(0, 100), seed=None):
    """
    Gera uma instância de problema TSP com cidades aleatórias e suas distâncias.
    """
    if seed is not None:
        np.random.seed(seed)

    # Gerar coordenadas aleatórias para as cidades
    cities = []
    for _ in range(num_cities):
        x = np.random.uniform(x_range[0], x_range[1])
        y = np.random.uniform(y_range[0], y_range[1])
        cities.append((x, y))
    
    # Calcular a matriz de distâncias euclidianas
    distances_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i == j:
                continue
            dist = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
            distances_matrix[i, j] = dist
            distances_matrix[j, i] = dist # Matriz simétrica
            
    return cities, distances_matrix

def save_tsp_instance(filename, cities, distances_matrix):
    """
    Salva uma instância TSP em um arquivo JSON.
    """
    data = {
        "num_cities": len(cities),
        "cities": cities,
        "distances_matrix": distances_matrix.tolist() # Converter numpy array para lista para JSON
    }
    filepath = os.path.join("data", "instances", filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Instância TSP salva em: {filepath}")

if __name__ == "__main__":
    # Exemplo de uso
    num_cities = 10
    cities, distances = generate_tsp_instance(num_cities, seed=42)
    print(f"Cidades geradas: {cities}")
    print(f"Matriz de Distâncias (parcial):\n{distances[:3, :3]}")
    
    save_tsp_instance("tsp_10_cities_seed42.json", cities, distances)
