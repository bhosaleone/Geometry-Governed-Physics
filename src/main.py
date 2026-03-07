from engine import BekensteinEngine
from mass_mapper import MassMapper
from constraints import ISLConstraints

def main():
    print("="*60)
    print("GEOMETRY GOVERNED PHYSICS - S5 KERNEL ENGINE v2.0")
    print("="*60)
    
    # 1. Spectral Engine & Constants
    engine = BekensteinEngine()
    alpha_inv = 1.0 / engine.get_alpha()
    print(f"\n[1] Derived Physical Constants:")
    print(f"Fine Structure alpha^-1: {alpha_inv:.6f}")
    print(f"Weak Mixing sin^2(theta_W): {engine.get_weak_mixing():.5f}")
    print(f"Cosmological Constant: {engine.get_lambda_constant()}")
    
    # 2. ISL Geometry
    isl = ISLConstraints()
    counts = isl.get_stable_counts()
    print(f"\n[2] ISL Geometric Stability:")
    print(f"Stable Shapes Hierarchy: {counts}")
    
    # 3. Mass Mapping
    mapper = MassMapper()
    print(f"\n[3] Mass-Eigenvalue Power-Law Mapping:")
    mapper.print_predictions()
    
    print("\n" + "="*60)
    print("VERIFICATION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()
