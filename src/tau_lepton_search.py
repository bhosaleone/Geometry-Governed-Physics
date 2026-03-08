import math

def tau_lepton_analysis():
    print("--- Tau Lepton Extended Mass Mapping Analysis ---")
    lambda_star = 28.64632726
    lambda_e = 20.0
    p_exponent = 9.381966
    alpha_inv = 137.035999
    alpha_em = 1.0 / alpha_inv

    target_ratio = 3477.15 # m_tau / m_e
    
    # We found no standard eigenvalue works.
    # What eigenvalue WOULD make n_eff = 0?
    
    # m_tau / m_e = ((lambda* - l_k) / (lambda* - lambda_e))^p
    # target_ratio^(1/p) = (lambda_star - l_k) / (lambda_star - lambda_e)
    
    l_k_zero_debt = lambda_star - (lambda_star - lambda_e) * (target_ratio ** (1.0 / p_exponent))
    print(f"To have n=0, lambda must be: {l_k_zero_debt:.3f}")
    
    print("\nLooking for integer n combinations:")
    for n in range(0, 15):
        m_geo_ratio = target_ratio / math.exp(n * alpha_em / (4 * math.pi))
        l_k = lambda_star - (lambda_star - lambda_e) * (m_geo_ratio ** (1.0 / p_exponent))
        print(f"n = {n:2d} => lambda = {l_k:.3f}")

if __name__ == "__main__":
    tau_lepton_analysis()
