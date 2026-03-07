import math

class LifetimeCalculator:
    """
    Implements the Geometric Particle Lifetime formula from GGP.
    Γ = ω₀ * exp(-n_max / n_eff)
    where n_max = S_max / (α/4π)
    """
    def __init__(self):
        # Universal Constants from GGP
        self.phi_total = 120
        self.alpha = 9 / (16 * (math.pi**(2.75)) * (self.phi_total**(0.25)))
        
        # Bekenstein-Compton maximum information debt
        # S_max = 2π at the Compton surface
        self.s_max = 2 * math.pi
        self.n_max = self.s_max / (self.alpha / (4 * math.pi))
        
        # Geometric clock ω₀ (Calibrated from Muon lifetime)
        # ω₀ ≈ 7.1 × 10^26 rad/s (approx 460 MeV scale)
        self.omega_0 = 7.1e26 

    def calculate_decay_rate(self, n_eff):
        """
        Calculates Γ = ω₀ * exp(-n_max / n_eff)
        For stable particles (n_eff integer), Γ -> 0 (geometric stability).
        For unstable (n_eff fractional), decay is triggered.
        """
        if n_eff <= 0:
            return 0
            
        # The stability theorem: Integer channels are self-closing (infinite budget)
        # In numerical sims, we check if n_eff is "perfectly" integer
        if abs(n_eff - round(n_eff)) < 1e-10:
            return 0 # Stable
            
        exponent = -self.n_max / n_eff
        return self.omega_0 * math.exp(exponent)

    def get_lifetime(self, n_eff):
        gamma = self.calculate_decay_rate(n_eff)
        if gamma == 0:
            return float('inf')
        return 1.0 / gamma

if __name__ == "__main__":
    calc = LifetimeCalculator()
    
    # Muon Case: n_eff = 19/8 (2.375)
    muon_n = 19/8
    muon_life = calc.get_lifetime(muon_n)
    
    print(f"--- GGP Lifetime Audit ---")
    print(f"Alpha (derived):  {1/calc.alpha:.6f}")
    print(f"Max Debt (n_max): {calc.n_max:.2f}")
    print(f"\n[Muon] (n=2.375):")
    print(f"Predicted Lifetime: {muon_life:.2e} s")
    print(f"Measured Lifetime:  2.20e-06 s")
    
    # Proton Case: n_eff = 4.0
    proton_n = 4.0
    proton_life = calc.get_lifetime(proton_n)
    print(f"\n[Proton] (n=4.0):")
    print(f"Stability Status: {'STABLE' if proton_life == float('inf') else 'DECAYING'}")
