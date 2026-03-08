import math

phi_total = 120
phi_gold = (1 + 5**0.5) / 2
alpha_inv = (16 * (math.pi**2.75) * (phi_total**0.25)) / 9
alpha = 1 / alpha_inv

omega_s = 7.32e26
omega_l = 7.10e22

# Let's see the ratio
ratio = omega_s / omega_l
print(f"Ratio omega_S / omega_L: {ratio:.2f}")

# Can we relate omega_s to Planck frequency?
# t_p = sqrt( hbar * G / c^5 ) = 5.39e-44 s
# omega_p = 1 / t_p = 1.85e43 rad/s
omega_p = 1.85487e43
print(f"Ratio omega_p / omega_s = {omega_p / omega_s:.2e}")

# Try S5 mixing time, Spectral gaps
# Could omega_l be derived from omega_s * alpha^something ?
# ratio is 10309.85
# alpha^-1 is 137.036
# alpha^-2 is 18778

print(f"alpha^-1: {alpha_inv:.3f}")
print(f"alpha^-2: {alpha_inv**2:.3f}")

# (omega_s / omega_l) vs alpha
val = alpha_inv * 75.2  # just checking
print(f"ratio / alpha_inv = {ratio / alpha_inv:.3f}")

# What if omega_l = omega_s * (m_e / m_p)?
m_p_ratio = 1836.15
m_mu_ratio = 206.77
print(f"Ratio vs m_p_ratio: {ratio / m_p_ratio:.3f}")

# is omega_s related to electron mass?
m_e_gev = 0.511e-3
m_p_gev = 0.938
print(f"omega_s corresponds to ~480 GeV. Ratio to m_p: {480 / m_p_gev:.2f}")

