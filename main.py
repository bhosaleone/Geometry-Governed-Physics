from src.mass_mapper import MassMapper
from src.lifetime_calc import LifetimeCalculator
from src.polarization_sim import ChiralitySimulator
from src.bekenstein_audit import run_holographic_audit
from src.chemical_audit import ChemicalAuditor
import sys

def run_grand_audit():
    print("\n" + "="*75)
    print("GEOMETRY GOVERNED PHYSICS: GRAND UNIFICATION AUDIT".center(75))
    print("="*75 + "\n")
    
    # 1. Mass mapping
    print("Layer 1: Power-Law Mass Mapping (L3, L10)")
    mapper = MassMapper()
    mapper.print_predictions()
    
    # 2. Holographic Audit
    print("\nLayer 2: Holographic Shadows & Bekenstein Limits (L16)")
    run_holographic_audit()
    
    # 3. Chemical Audit
    print("\nLayer 3: Geometric Chemistry (L19)")
    chem = ChemicalAuditor()
    chem.run()
    
    print("\nLayer 4: Light Geometry & S5 Parity")
    chirality = ChiralitySimulator()
    chirality.run_audit()
    
    print("\n" + "="*80)
    print("AUDIT COMPLETE: THE GEOMETRY IS GOVERNED".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    run_grand_audit()
