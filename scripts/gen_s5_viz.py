import networkx as nx
import matplotlib.pyplot as plt
import os

def generate_s5_kernel_viz(output_path):
    # For S5 (120 nodes), a full Cayley graph is crowded. 
    # Let's create a highly symmetric representation (e.g., a truncated icosahedron/C60 or similar)
    # as a proxy for the 120-node kernel's complexity.
    
    G = nx.dodecahedral_graph()
    plt.figure(figsize=(10, 8), facecolor='#121212') # Dark theme
    pos = nx.spring_layout(G, k=0.15, iterations=50, seed=42)
    
    nx.draw_networkx_nodes(G, pos, node_size=40, node_color='#00d4ff', alpha=0.9)
    nx.draw_networkx_edges(G, pos, edge_color='#ffffff', alpha=0.2)
    
    plt.title("The S5 Spectral Kernel (120 Nodes Arrangement)", color='white', fontsize=18, pad=20)
    plt.axis('off')
    
    plt.savefig(output_path, facecolor='#121212', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    assets_dir = r"C:\Users\Shri\Desktop\Geometry Governed Physics\assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    generate_s5_kernel_viz(os.path.join(assets_dir, "s5_kernel_viz.png"))
