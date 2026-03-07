import networkx as nx
import numpy as np
from itertools import permutations

def get_spectrum():
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
    
    # 5-cycle (12345) and (54321)
    generators.append((1, 2, 3, 4, 0))
    generators.append((4, 0, 1, 2, 3))
    
    # Build Graph
    G = nx.Graph()
    for p in s5:
        for g in generators:
            # Compose p and g
            neighbor = tuple(p[i] for i in g)
            G.add_edge(p, neighbor)
            
    # Compute Laplacian Spectrum
    L = nx.laplacian_matrix(G).toarray()
    eigenvalues = np.linalg.eigvalsh(L)
    
    # Group by multiplicity
    unique_vals = []
    counts = []
    for val in eigenvalues:
        rounded = round(val, 8)
        if not unique_vals or rounded > unique_vals[-1] + 1e-6:
            unique_vals.append(rounded)
            counts.append(1)
        else:
            counts[-1] += 1
            
    print(f"Nodes: {len(s5)}")
    print(f"Degree: {len(generators)}")
    print("\n--- S5 Laplacian Spectrum ---")
    print(f"{'Eigenvalue':<12} | {'Multiplicity'}")
    print("-" * 25)
    for v, c in zip(unique_vals, counts):
        print(f"{v:<12.8f} | {c}")

if __name__ == "__main__":
    get_spectrum()
