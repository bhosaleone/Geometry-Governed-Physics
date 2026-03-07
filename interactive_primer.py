import math
import time
import sys

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    # Set encoding to utf-8 for special characters
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    print("\n" + "="*70)
    print("Welcome to the Geometry-First Physics Interactive Primer!")
    print("="*70 + "\n")
    
    slow_print("The 'One Object' ($S_5$) has exactly 120 closure states.")
    input("[Press Enter to solve the Universe Scale...]")
    
    print("\n" + "-"*40)
    slow_print("The S5 Stability-Duality Theorem")
    
    phi_total = 120
    base = 90 / math.pi
    correction = 3 / (16 * phi_total)
    lambda_star = base - correction
    
    slow_print(f"1. Continuum Base (90/π):   {base:.8f}")
    slow_print(f"2. Group Correction (1/640): {correction:.8f}")
    slow_print(f"3. Derived λ*:               {lambda_star:.8f}")
    
    print("\n" + "-"*40)
    slow_print("Predicting the Proton Mass Ratio")
    
    # Constants
    phi_gold = (1 + 5**0.5) / 2
    lambda_p = 9 + 1/(phi_gold**2)
    lambda_e = 20.0
    alpha = 1 / 137.036
    
    # Power Law mapping
    m_geo = ((lambda_star - lambda_p) / (lambda_star - lambda_e))**lambda_p
    # existence correction (n=4)
    m_final = m_geo * math.exp(4 * alpha / (4 * math.pi))
    
    slow_print(f"Calculated: {m_final:.4f}")
    slow_print(f"Measured:   1836.1527")
    slow_print(f"Precision:  {100 * (1 - abs(m_final - 1836.1527)/1836.1527):.5f}%")
    
    print("\n" + "="*70)
    slow_print("Geometry is the final answer. Physics is just the calculation.")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
