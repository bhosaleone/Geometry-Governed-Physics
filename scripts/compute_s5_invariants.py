import networkx as nx
import itertools

def get_s5_cayley():
    # Elements of S5
    elements = list(itertools.permutations(range(5)))
    elem_to_idx = {p: i for i, p in enumerate(elements)}
    
    # Generators
    generators = []
    # All transpositions (10)
    for i in range(5):
        for j in range(i + 1, 5):
            p = list(range(5))
            p[i], p[j] = p[j], p[i]
            generators.append(tuple(p))
            
    # 5-cycle (12345) and inverse (54321) - using 0-indexed: (01234)
    # Forward 5-cycle
    p_f = [1, 2, 3, 4, 0]
    generators.append(tuple(p_f))
    # Backward 5-cycle
    p_b = [4, 0, 1, 2, 3]
    generators.append(tuple(p_b))
    
    def compose(p1, p2):
        return tuple(p1[p2[i]] for i in range(5))

    G = nx.Graph()
    for e in elements:
        for g in generators:
            neighbor = compose(e, g)
            G.add_edge(elem_to_idx[e], elem_to_idx[neighbor])
            
    return G

if __name__ == "__main__":
    G = get_s5_cayley()
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Degree: {G.degree(0)}")
    
    diameter = nx.diameter(G)
    print(f"Diameter: {diameter}")
    
    avg_clustering = nx.average_clustering(G)
    print(f"Average Clustering: {avg_clustering}")
    
    # Calculate triangles
    total_triangles = sum(nx.triangles(G).values()) // 3
    print(f"Total Triangles: {total_triangles}")
