import math

def s6_mass_evaluation():
    print("--- Evaluating S6 Extension for Heavy Masses ---")
    
    # Fundamental constants from S5 continue as universal limits
    lambda_star = 28.64632726
    lambda_e = 20.0
    p_exponent = 9.381966
    alpha_inv = 137.035999
    alpha_em = 1.0 / alpha_inv

    # The new S6 Eigenvalues (from computational script)
    s6_eigenvalues = [0, 6, 10, 12, 15, 18, 20, 24, 30]
    
    # 1. W Boson Test
    w_target_ratio = 157433.0
    print("\n--- 1. W BOSON EVALUATION ---")
    print(f"Target m_W / m_e = {w_target_ratio:.2f}")
    
    for l_k in s6_eigenvalues:
        if l_k == 30: # 30 breaks lambda_star limit for geometric mass (lambda_star - 30) < 0
            break
            
        ratio = (lambda_star - l_k) / (lambda_star - lambda_e)
        if ratio <= 0:
            continue
            
        m_geo_ratio = ratio ** p_exponent
        
        # Calculate required emergence debt n
        n_eff = math.log(w_target_ratio / m_geo_ratio) * (4 * math.pi) / alpha_em
        
        print(f"S6 lambda={l_k:<4} -> m_geo_ratio={m_geo_ratio:10.5f} -> required n_eff={n_eff:10.3f}")

    # 2. Tau Lepton Test
    tau_target_ratio = 3477.15
    print("\n--- 2. TAU LEPTON EVALUATION ---")
    print(f"Target m_tau / m_e = {tau_target_ratio:.2f}")
    
    for l_k in s6_eigenvalues:
        if l_k == 30: # 30 breaks lambda_star limit for geometric mass
            break
            
        ratio = (lambda_star - l_k) / (lambda_star - lambda_e)
        if ratio <= 0:
            continue
            
        m_geo_ratio = ratio ** p_exponent
        
        # Calculate required emergence debt n
        n_eff = math.log(tau_target_ratio / m_geo_ratio) * (4 * math.pi) / alpha_em
        
        print(f"S6 lambda={l_k:<4} -> m_geo_ratio={m_geo_ratio:10.5f} -> required n_eff={n_eff:10.3f}")


if __name__ == "__main__":
    s6_mass_evaluation()
