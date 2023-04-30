import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
substrate_concentration = np.array([1.5, 2.0, 3.0, 4.0, 8.0, 16.0])
product_formation = np.array([0.21, 0.24, 0.28, 0.33, 0.40, 0.45])
multiplier = 1e-6

product_formation = np.multiply(product_formation, multiplier)


# Michaelis-Menten equation function
def michaelis_menten(S, Vmax, Km):
    return Vmax * S / (Km + S)


# Fit the Michaelis-Menten equation
params, _ = curve_fit(michaelis_menten, substrate_concentration, product_formation)
Vmax_fit, Km_fit = params

# Direct coordinates (Michaelis-Menten equation)
plt.plot(substrate_concentration, product_formation, linestyle='-', marker='o', label="Michaelis-Menten")
plt.xlabel('Substrate Concentration [S] (moles)')
plt.ylabel('Product Formation (moles/min)')
plt.title('Michaelis-Menten Plot')

x = np.linspace(min(substrate_concentration), max(substrate_concentration), 100)
y = michaelis_menten(x, Vmax_fit, Km_fit)
plt.plot(x, y, label="Fitted Curve")

plt.legend()
plt.show()

# Print Vmax and Km
print("Vmax (Curve fitting):", Vmax_fit, "micromoles/min")
print("Km (Curve fitting):", Km_fit, "moles")
median = np.median(product_formation)

# Inverse coordinates (Lineweaver-Burk equation)
inv_product_formation = 1 / product_formation
inv_substrate_concentration = 1 / substrate_concentration

plt.plot(inv_substrate_concentration, inv_product_formation, 'o', label="Lineweaver-Burk")
plt.xlabel('1 / [S] (1/moles)')
plt.ylabel('1 / V (min/moles)')
plt.title('Lineweaver-Burk Plot')
plt.legend()

# Linear regression for Lineweaver-Burk plot
slope, intercept = np.polyfit(inv_substrate_concentration, inv_product_formation, 1)
x = np.linspace(0, max(inv_substrate_concentration), 100)
y = slope * x + intercept
plt.plot(x, y)

plt.show()

# Calculate Vmax and Km
Vmax = 1 / intercept
Km = slope / intercept

print("Lineweaver-Burk Vmax:", Vmax, "moles/min")
print("Lineweaver-Burk Km:", Km, "moles")

# V - V/[S] (Eadie-Hofstee equation)
V_div_S = product_formation / substrate_concentration

plt.plot(V_div_S, product_formation, 'o', label="Eadie-Hofstee")
plt.xlabel('V/[S] (min^(-1))')
plt.ylabel('V (moles/min)')
plt.title('Eadie-Hofstee Plot')
plt.legend()

# Linear regression for Eadie-Hofstee plot
slope, intercept = np.polyfit(V_div_S, product_formation, 1)
x = np.linspace(min(V_div_S), max(V_div_S))
y = slope * x + intercept
plt.plot(x, y)

plt.show()

# Calculate Vmax and Km
Vmax = intercept
Km = slope

print("Eadie-Hofstee Vmax:", Vmax, "moles/min")
print("Eadie-Hofstee Km:", -Km, "moles")
