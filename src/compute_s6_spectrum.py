import networkx as nx
import numpy as np
import scipy.sparse.linalg as sla
from scipy.sparse import csr_matrix
from itertools import permutations

def compute_s6_spectrum():
    print("--- S6 Spectral Computation ---")
    
    # 1. Elements of S6
    elements = list(permutations(range(6)))
    print(f"|S6| = {len(elements)} (Nodes)")
    
    # 2. Generators: All transpositions (15 transpositions for S6)
    generators = []
    id_perm = tuple(range(6))
    for i in range(6):
        for j in range(i + 1, 6):
            p = list(id_perm)
            p[i], p[j] = p[j], p[i]
            generators.append(tuple(p))
            
    print(f"Number of Generators (Degree) = {len(generators)}")
    
    # Alternatively, 15 transpositions + two 6-cycles? 
    # Let's stick to just the 15 transpositions (standard Cayley graph).
    
    # Create index mapping
    elem_to_idx = {p: i for i, p in enumerate(elements)}
    
    # 3. Build Adjacency Matrix
    N = len(elements)
    row = []
    col = []
    
    for e in elements:
        e_idx = elem_to_idx[e]
        for g in generators:
            neighbor = tuple(e[i] for i in g)
            neighbor_idx = elem_to_idx[neighbor]
            row.append(e_idx)
            col.append(neighbor_idx)
            
    # Data is all 1s
    data = np.ones(len(row))
    A = csr_matrix((data, (row, col)), shape=(N, N))
    
    # Laplacian L = D - A
    D = csr_matrix((np.array([len(generators)] * N), (np.arange(N), np.arange(N))), shape=(N, N))
    L = D - A
    
    # 4. Compute Eigenvalues
    # For a 720x720 matrix, dense eigenvalue computation is fast enough
    L_dense = L.toarray()
    eigenvalues = np.linalg.eigvalsh(L_dense)
    
    unique_vals = []
    counts = []
    for val in eigenvalues:
        rounded = round(val, 6)
        # Avoid near-zero negative values floating point issues
        if rounded <= 1e-6:
            rounded = 0.0
            
        if not unique_vals or rounded > unique_vals[-1] + 1e-4:
            unique_vals.append(rounded)
            counts.append(1)
        else:
            counts[-1] += 1
            
    print("\n--- S6 Laplacian Eigenvalues (Transpositions) ---")
    print(f"{'Eigenvalue':<12} | {'Multiplicity'}")
    print("-" * 25)
    for v, c in zip(unique_vals, counts):
        print(f"{v:<12.5f} | {c}")
        
    # Return eigenvalues for physics matching
    return unique_vals

if __name__ == "__main__":
    compute_s6_spectrum()
