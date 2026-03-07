import numpy as np
import matplotlib.pyplot as plt
import os

def generate_mass_mapping_plot(output_path):
    # v2.0 Constants
    lambda_star = 28.6513
    lambda_e = 20.0
    phi = (1 + 5**0.5) / 2
    p = 9 + 1/(phi**2)
    
    lambdas = np.linspace(5, 20.1, 500)
    # m_geo/m_e = ((lambda* - lambda_k) / (lambda* - lambda_e))^p
    mass_ratios = ((lambda_star - lambdas) / (lambda_star - lambda_e))**p
    
    plt.figure(figsize=(10, 6), facecolor='#121212')
    plt.gca().set_facecolor('#121212')
    
    plt.plot(lambdas, mass_ratios, color='#00d4ff', linewidth=3, label='Power-Law Mapping')
    
    # Highlight particles
    particles = [
        ("Electron", 20.0, 1.0, '#ffcc00'),
        ("Muon", 13.382, 206.77, '#ff3366'),
        ("Proton", 9.382, 1836.15, '#33ff99')
    ]
    
    for name, l, m, color in particles:
        plt.scatter(l, m, color=color, s=150, zorder=5, label=name)
        plt.annotate(name, (l, m), textcoords="offset points", xytext=(10,10), 
                     color=color, fontsize=12, fontweight='bold')
    
    plt.yscale('log') # Log scale for better visibility
    plt.xlabel("Eigenvalue (λ)", color='white', fontsize=14)
    plt.ylabel("Mass Ratio (m/m_e)", color='white', fontsize=14)
    plt.title("The Music of Reality: Mass Resonance Curve", color='white', fontsize=18, pad=20)
    
    # Customize grid
    plt.grid(True, which='both', linestyle='--', alpha=0.3, color='gray')
    ax = plt.gca()
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')
        
    plt.legend(facecolor='#121212', edgecolor='white', labelcolor='white')
    
    plt.savefig(output_path, facecolor='#121212', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    assets_dir = r"C:\Users\Shri\Desktop\Geometry Governed Physics\assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    generate_mass_mapping_plot(os.path.join(assets_dir, "mass_mapping_plot.png"))
