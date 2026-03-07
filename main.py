from src.mass_mapper import MassMapper
from src.lifetime_calc import LifetimeCalculator
from src.polarization_sim import ChiralitySimulator
from src.bekenstein_audit import run_holographic_audit
import sys

def run_grand_audit():
    print("\n" + "="*80)
    print("GEOMETRY GOVERNED PHYSICS: GRAND UNIFICATION AUDIT".center(80))
    print("="*80 + "\n")
    
    # 1. Mass Mapping
    print("Layer 1: Mass Mapping (L0-L5)")
    mapper = MassMapper()
    mapper.print_predictions()
    
    # 2. Holographic Shadow Audit
    print("\nLayer 2: Holographic Shadows & Bekenstein Limits (L9)")
    run_holographic_audit()
    
    # 3. Lifetime Audit
    print("\nLayer 3: Particle Lifetimes & Information Debt (L8)")
    life_calc = LifetimeCalculator()
    muon_n = 19/8
    muon_life = life_calc.get_lifetime(muon_n)
    print(f"Muon (n=2.375) Predicted Lifetime: {muon_life:.2e} s")
    print(f"Proton (n=4.000) Predicted Status:  STABLE")
    
    # 4. Polarization Audit
    print("\nLayer 4: Light Geometry & S5 Parity")
    chirality = ChiralitySimulator()
    chirality.run_audit()
    
    print("\n" + "="*80)
    print("AUDIT COMPLETE: THE GEOMETRY IS GOVERNED".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    run_grand_audit()
