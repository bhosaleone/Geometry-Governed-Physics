import networkx as nx
import itertools

def get_s5_cayley(generators):
    elements = list(itertools.permutations(range(5)))
    elem_to_idx = {p: i for i, p in enumerate(elements)}
    
    def compose(p1, p2):
        return tuple(p1[p2[i]] for i in range(5))

    G = nx.Graph()
    for e in elements:
        for g in generators:
            neighbor = compose(e, g)
            G.add_edge(elem_to_idx[e], elem_to_idx[neighbor])
    return G

def test_generators():
    # 1. Full Transpositions (10) + 5-cycle + inverse = 12
    gens_12 = []
    for i in range(5):
        for j in range(i + 1, 5):
            p = list(range(5)); p[i], p[j] = p[j], p[i]
            gens_12.append(tuple(p))
    p_f = [1, 2, 3, 4, 0]; gens_12.append(tuple(p_f))
    p_b = [4, 0, 1, 2, 3]; gens_12.append(tuple(p_b))
    
    # 2. Are there 9? Maybe only the 10 transpositions - 1? Or something else.
    # Let's just check the 12-set first for 4-cycles.
    G = get_s5_cayley(gens_12)
    print(f"Set 12: Nodes={G.number_of_nodes()}, Degree={G.degree(0)}")
    
    # Compute 4-cycles
    # A^4 trace / 8 - (adjustment for edges/2-cycles)
    # Or more simply:
    A = nx.adjacency_matrix(G)
    A2 = A @ A
    A4 = A2 @ A2
    # Number of 4-cycles = (Tr(A^4) - 8*E - 4*sum(d(d-1))) / 8
    trA4 = A4.diagonal().sum()
    E = G.number_of_edges()
    sum_d_d1 = sum(d*(d-1) for n, d in G.degree())
    cycles4 = (trA4 - 8*E - 4*sum_d_d1) / 8
    print(f"4-cycles: {cycles4}")
    
    # 4-cycle density (possible 4-cycles)
    # For a d-regular graph, max 4-cycles per node is roughly d(d-1)/2 ? No.
    print(f"4-cycles per node: {cycles4 / 120}")

if __name__ == "__main__":
    test_generators()
