import networkx as nx
import itertools

def get_s5_cayley():
    elements = list(itertools.permutations(range(5)))
    elem_to_idx = {p: i for i, p in enumerate(elements)}
    
    generators = []
    # 10 transpositions
    for i in range(5):
        for j in range(i + 1, 5):
            p = list(range(5)); p[i], p[j] = p[j], p[i]
            generators.append(tuple(p))
    # 5-cycle and inverse
    p_f = [1, 2, 3, 4, 0]; generators.append(tuple(p_f))
    p_b = [4, 0, 1, 2, 3]; generators.append(tuple(p_b))
    
    def compose(p1, p2):
        return tuple(p1[p2[i]] for i in range(5))

    G = nx.Graph()
    for e in elements:
        for g in generators:
            neighbor = compose(e, g)
            G.add_edge(elem_to_idx[e], elem_to_idx[neighbor])
    return G

def count_4_cycles_node(G, node_idx):
    # Number of 4-cycles containing node_idx
    # Path: node_idx -> a -> b -> c -> node_idx
    # node_idx != a != b != c != node_idx
    count = 0
    neighbors = list(G.neighbors(node_idx))
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            u = neighbors[i]
            v = neighbors[j]
            # Find common neighbors of u and v other than node_idx
            common = set(G.neighbors(u)) & set(G.neighbors(v))
            common.discard(node_idx)
            count += len(common)
    return count // 2 # Each 4-cycle counted once per node? No.
    # Paths u-v-w-x-u. For a fixed x, u and w are neighbors.
    # The common neighbors of u and w are x and v.
    # So for fixed x, picking u and w (neighbors of x), their common neighbors (besides x) are the possible v's.
    # The sum counts each (u,x,w) corner. Each cycle has 4 corners. 
    # Actually, the above loop counts each cycle once per node.

if __name__ == "__main__":
    G = get_s5_cayley()
    c4 = count_4_cycles_node(G, 0)
    print(f"4-cycles per node: {c4}")
    
    # Total 4-cycles
    total_c4 = c4 * 120 / 4
    print(f"Total 4-cycles: {total_c4}")
    
    # 4-cycle density (normalized)
    # Max possible 4-cycles per node is (d*(d-1))/2 ? No.
    # For a grid it's 1. 
    d = 12
    max_c4_node = (d * (d - 1)) // 2 # If every pair of neighbors has a common 4th node
    print(f"Max 4-cycles per node (approx): {max_c4_node}")
    print(f"C4/Max: {c4 / max_c4_node}")
