import matplotlib.pyplot as plt
import os

def generate_spectrum_viz(output_path):
    # S5 Irrep Spectrum
    levels = {
        'Trivial': 0,
        'Gap (λ1)': 6.382,
        'Tau (τ)': 8.000,
        'Proton (p)': 9.382,
        'Muon (μ)': 13.382,
        'Electron (e)': 20.000
    }
    
    plt.figure(figsize=(10, 4), facecolor='#121212')
    plt.gca().set_facecolor('#121212')
    
    for name, val in levels.items():
        color = '#00d4ff' if 'λ' in name or 'Trivial' in name else '#ffcc00'
        plt.axvline(x=val, color=color, linewidth=4, alpha=0.8)
        plt.text(val, 0.5, f"  {name}\n  ({val:.3f})", color='white', rotation=0, verticalalignment='center', fontsize=10)
    
    plt.xlim(-1, 22)
    plt.ylim(0, 1)
    plt.yticks([]) # Hide Y axis
    plt.title("S5 Kernel: Allowed Vibration Spectrum", color='white', fontsize=18, pad=20)
    plt.xlabel("Eigenvalue Level (λ)", color='white', fontsize=14)
    
    ax = plt.gca()
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')
    
    plt.savefig(output_path, facecolor='#121212', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    assets_dir = r"C:\Users\Shri\Desktop\Geometry Governed Physics\assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    generate_spectrum_viz(os.path.join(assets_dir, "spectrum_viz.png"))
