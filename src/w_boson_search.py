import math

lambda_star = 28.64632726
lambda_e = 20.0
p_exponent = 9.381966
alpha_inv = 137.035999
alpha_em = 1.0 / alpha_inv

target_ratio = 157433.0

known_eigenvalues = [0, 3, 5, 6, 8, 9.381966, 10, 12, 13, 13.381966, 15, 18, 20]

def test_inverted_mapping():
    print("Testing Inverted Mapping: m_W / m_e = ((lambda* - lambda_e) / (lambda* - lambda_k))^p * exp(...)")
    for n in range(-5, 5):
        emergence = math.exp(n * alpha_em / (4 * math.pi))
        base_ratio = target_ratio / emergence
        
        # base_ratio = ((lambda_star - lambda_e) / (lambda_star - lambda_k))^p
        # base_ratio^(1/p) = (lambda_star - lambda_e) / (lambda_star - lambda_k)
        # lambda_star - lambda_k = (lambda_star - lambda_e) / (base_ratio^(1/p))
        # lambda_k = lambda_star - (lambda_star - lambda_e) / (base_ratio^(1/p))
        
        val = base_ratio ** (1.0 / p_exponent)
        lambda_k = lambda_star - (lambda_star - lambda_e) / val
        
        print(f"n = {n:2d}: Required lambda_k = {lambda_k:.6f}")
        for k in known_eigenvalues:
            if abs(lambda_k - k) < 0.1:
                print(f"  -> CLOSE MATCH to known eigenvalue {k}!")

def test_standard_mapping_bosonic():
    print("\nTesting Standard Mapping but finding required lambda_k without assumption of negativity:")
    for n in range(-5, 15):
        emergence = math.exp(n * alpha_em / (4 * math.pi))
        base_ratio = target_ratio / emergence
        val = base_ratio ** (1.0 / p_exponent)
        lambda_k = lambda_star - (lambda_star - lambda_e) * val
        print(f"n = {n:2d}: Required lambda_k = {lambda_k:.6f}")

print("--- W Boson Search ---")
test_inverted_mapping()
test_standard_mapping_bosonic()
