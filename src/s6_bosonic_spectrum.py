import numpy as np
import scipy.sparse.linalg as sla
from scipy.sparse import csr_matrix
from itertools import permutations

def compute_bosonic_spectrum():
    print("--- Computing the Bosonic (Triple-Transposition) Spectrum in S6 ---")
    
    # 1. Elements of S6
    elements = list(permutations(range(6)))
    elem_to_idx = {p: i for i, p in enumerate(elements)}
    
    # 2. Generators: Triple-transpositions
    # A triple transposition consists of three disjoint 2-cycles, e.g., (12)(34)(56)
    def count_cycles(p):
        visited = set()
        cycles = []
        for i in range(6):
            if i not in visited:
                cycle_len = 0
                curr = i
                while curr not in visited:
                    visited.add(curr)
                    curr = p[curr]
                    cycle_len += 1
                cycles.append(cycle_len)
        return sorted(cycles)

    generators_bosonic = [p for p in elements if count_cycles(p) == [2, 2, 2]]
    print(f"Number of Bosonic Generators (Triple-Transpositions) = {len(generators_bosonic)}")
    
    # 3. Build Adjacency Matrix
    N = len(elements)
    row = []
    col = []
    
    for e in elements:
        e_idx = elem_to_idx[e]
        for g in generators_bosonic:
            neighbor = tuple(e[g[i]] for i in range(6))
            neighbor_idx = elem_to_idx[neighbor]
            row.append(e_idx)
            col.append(neighbor_idx)
            
    data = np.ones(len(row))
    A = csr_matrix((data, (row, col)), shape=(N, N))
    
    # Laplacian L = D - A
    D = csr_matrix((np.array([len(generators_bosonic)] * N), (np.arange(N), np.arange(N))), shape=(N, N))
    L = D - A
    
    # 4. Compute Eigenvalues
    L_dense = L.toarray()
    eigenvalues = np.linalg.eigvalsh(L_dense)
    
    unique_vals = []
    counts = []
    for val in eigenvalues:
        rounded = round(val, 5)
        if rounded <= 1e-5:
            rounded = 0.0
            
        if not unique_vals or rounded > unique_vals[-1] + 1e-4:
            unique_vals.append(rounded)
            counts.append(1)
        else:
            counts[-1] += 1
            
    print("\n--- S6 Bosonic Laplacian Eigenvalues ---")
    print(f"{'Eigenvalue':<12} | {'Multiplicity'}")
    print("-" * 25)
    for v, c in zip(unique_vals, counts):
        print(f"{v:<12.5f} | {c}")

if __name__ == "__main__":
    compute_bosonic_spectrum()
