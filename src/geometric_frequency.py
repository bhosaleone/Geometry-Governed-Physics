import networkx as nx
import numpy as np
import math
from itertools import permutations

def get_s5_spectrum_and_gap():
    # S5 elements
    s5 = list(permutations(range(5)))
    id_perm = tuple(range(5))
    
    # Generators: all transpositions (10) + 5-cycle (12345) and its inverse
    # Total 12 generators
    generators = []
    # Transpositions (10)
    for i in range(5):
        for j in range(i + 1, 5):
            p = list(id_perm)
            p[i], p[j] = p[j], p[i]
            generators.append(tuple(p))
    
    generators.append((1, 2, 3, 4, 0))
    generators.append((4, 0, 1, 2, 3))
    
    G = nx.Graph()
    for p in s5:
        for g in generators:
            neighbor = tuple(p[i] for i in g)
            G.add_edge(p, neighbor)
            
    # Compute Normalized Laplacian = I - D^{-1/2} A D^{-1/2}
    L_norm = nx.normalized_laplacian_matrix(G).toarray()
    eigenvalues = np.linalg.eigvalsh(L_norm)
    
    # Sort eigenvalues. For normalized Laplacian, values are between 0 and 2.
    # The smallest is 0. The second smallest is the spectral gap (lambda_2).
    eigenvalues = sorted([round(v, 8) for v in eigenvalues])
    unique_vals = sorted(list(set(eigenvalues)))
    
    spectral_gap = 0
    for v in unique_vals:
        if v > 1e-6:
            spectral_gap = v
            break
            
    print(f"Degree of graph: {G.degree(id_perm)}")
    print(f"Normalized Spectral gap: {spectral_gap:.8f}")
    
    # Random Walk Mixing Time (Relaxation time) -> t_rel = 1 / spectral_gap
    t_rel = 1.0 / spectral_gap
    print(f"Relaxation Time (t_rel): {t_rel:.4f} steps")
    
    # For a graph of 120 nodes, mixing time to be epsilon close to stationary is bounded by:
    # t_mix <= t_rel * ln(120 / epsilon)
    # Let's say epsilon is the fine structure constant alpha? or 1/137?
    
    alpha_inv = 137.036
    alpha = 1.0 / alpha_inv
    t_mix_alpha = t_rel * math.log(120 / alpha)
    
    print(f"Mixing Time bound (eps = alpha): {t_mix_alpha:.4f} steps")

if __name__ == "__main__":
    get_s5_spectrum_and_gap()
