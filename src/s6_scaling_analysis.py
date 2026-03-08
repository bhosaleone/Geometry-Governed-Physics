import math

def s6_scaling_analysis():
    print("--- S6 Mass Mapping Analysis: Unscaled vs. Scaled ---\n")
    
    # 1. CONSTANTS
    target_W = 157433.0
    target_tau = 3477.15
    s6_eigenvalues = [0, 6, 10, 12, 15, 18, 20, 24, 30]
    
    # Fundamental constants from S5 (Unscaled)
    phi_s5 = 120
    lambda_e_s5 = 20.0
    p_s5 = 9.381966  # Represents Proton stiffness in S5
    
    alpha_inv_s5 = (16 * (math.pi**2.75) * (phi_s5**0.25)) / 9
    alpha_s5 = 1.0 / alpha_inv_s5
    lambda_star_s5 = (90 / math.pi) - (3 / (16 * phi_s5)) # ~28.646

    # 2. SCALED CONSTANTS FOR S6
    # If the Phase-Field Engine scales purely with |S|:
    phi_s6 = 720
    
    # Assume alpha scales structurally with phi
    alpha_inv_s6 = (16 * (math.pi**2.75) * (phi_s6**0.25)) / 9
    alpha_s6 = 1.0 / alpha_inv_s6
    
    # Assume lambda_star scales with phi
    lambda_star_s6 = (90 / math.pi) - (3 / (16 * phi_s6))
    
    # We must determine the "Electron" and "Proton" base equivalents in S6.
    # What is lambda_e in S6? It's the maximum eigenvalue of the standard embedding.
    # For now, let's keep lambda_e = 20 (assuming the electron mode embeds stably in S6)
    # and p = 9.38 (assuming proton stability is a universal invariant).
    # IF p and lambda_e scale, they would scale by the spectrum ratio (30/20 = 1.5).
    # Let's test a purely symmetric 1.5x structural scaling:
    lambda_e_s6 = 20.0 * 1.5   # 30.0 (The new max eigenvalue)
    p_s6 = 9.381966 * 1.5      # 14.0729
    lambda_star_s6_geom = lambda_star_s5 * 1.5 # ~42.969
    
    # 3. EVALUATION FUNCTION
    def evaluate_mapping(name, target, lambda_star, lambda_e, p, alpha, scale_name):
        print(f"[{scale_name}] Evaluation for {name} (Target Ratio: {target})")
        print(f"Parameters: lambda*={lambda_star:.3f}, lambda_e={lambda_e:.3f}, p={p:.3f}, alpha^-1={1/alpha:.3f}")
        
        best_match = None
        min_n_diff = float('inf')
        
        for l_k in s6_eigenvalues:
            if lambda_star - l_k <= 0:
                continue
            if lambda_star - lambda_e <= 0:
                continue
                
            ratio = (lambda_star - l_k) / (lambda_star - lambda_e)
            if ratio <= 0:
                continue
                
            m_geo = ratio ** p
            
            # target = m_geo * exp(n * alpha / 4pi)
            n_eff = math.log(target / m_geo) * (4 * math.pi) / alpha
            
            # We want an n as close to zero or a small integer/fraction as possible
            print(f"  lambda={l_k:<4} -> m_geo={m_geo:10.2f} -> required n_eff={n_eff:8.3f}")
            
            if abs(n_eff) < min_n_diff:
                min_n_diff = abs(n_eff)
                best_match = (l_k, n_eff)
                
        print(f"  Best geometric fit: lambda={best_match[0]}, residual n={best_match[1]:.3f}\n")
        return best_match

    # 4. RUN TESTS
    print("================== W BOSON ==================")
    evaluate_mapping("W Boson", target_W, lambda_star_s5, lambda_e_s5, p_s5, alpha_s5, "UNSCALED (S5 Params + S6 Eigs)")
    evaluate_mapping("W Boson", target_W, lambda_star_s6_geom, lambda_e_s6, p_s6, alpha_s6, "SCALED (1.5x S6 Params + S6 Eigs)")

    print("================== TAU LEPTON ==================")
    evaluate_mapping("Tau Lepton", target_tau, lambda_star_s5, lambda_e_s5, p_s5, alpha_s5, "UNSCALED (S5 Params + S6 Eigs)")
    evaluate_mapping("Tau Lepton", target_tau, lambda_star_s6_geom, lambda_e_s6, p_s6, alpha_s6, "SCALED (1.5x S6 Params + S6 Eigs)")

if __name__ == "__main__":
    s6_scaling_analysis()
