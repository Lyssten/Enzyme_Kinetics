import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
substrate_concentration = np.array([0.5, 1.0, 1.5, 2.5, 3.5])
product_formation_with_inhibition = np.array([16.67, 25.25, 30.49, 37.04, 38.91])
product_formation = np.array([23.5, 32.2, 36.9, 41.8, 44.0])

# Michaelis-Menten equation function
def michaelis_menten(S, Vmax, Km):
    return Vmax * S / (Km + S)


# Fit the Michaelis-Menten equation
params, _ = curve_fit(michaelis_menten, substrate_concentration, product_formation)
Vmax_fit, Km_fit = params

params_inh, _ = curve_fit(michaelis_menten, substrate_concentration, product_formation_with_inhibition)
Vmax_fit_inh, Km_fit_inh = params_inh

# Direct coordinates (Michaelis-Menten equation)
plt.plot(substrate_concentration, product_formation, linestyle='-', marker='o', label="Michaelis-Menten")
plt.plot(substrate_concentration, product_formation_with_inhibition, linestyle='-', marker='o',
         label="Michaelis-Menten-Inhibition")

plt.xlabel('Substrate Concentration [S] (mmol)')
plt.ylabel('Product Formation (mmol/min)')
plt.title('Michaelis-Menten Plot')

x = np.linspace(min(substrate_concentration), max(substrate_concentration), 100)
y = michaelis_menten(x, Vmax_fit, Km_fit)
plt.plot(x, y, label="Fitted Curve")

x_inh = x
y_inh = michaelis_menten(x_inh, Vmax_fit_inh, Km_fit_inh)
plt.plot(x_inh, y_inh, label="Fitted Curve with inhibition")

plt.legend()
plt.show()

# Print Vmax and Km
print("Michaelis-Menten Vmax: ", round(Vmax_fit, 3), "mmol/min")
print("Michaelis-Menten Km:", round(Km_fit, 3), "mmol")

print("Michaelis-Menten with inhibition Vmax:", round(Vmax_fit, 3), "mmol/min")
print("Michaelis-Menten with inhibition Km:", round(Km_fit_inh, 3), "mmol")

# Inverse coordinates (Lineweaver-Burk equation)
inv_product_formation = 1 / product_formation
inv_substrate_concentration = 1 / substrate_concentration

inv_product_formation_inh = 1 / product_formation_with_inhibition

plt.plot(inv_substrate_concentration, inv_product_formation, 'o', label="Lineweaver-Burk")
plt.plot(inv_substrate_concentration, inv_product_formation_inh, 'o', label="Lineweaver-Burk with inhibition")

plt.xlabel('1 / [S] (1/mmol)')
plt.ylabel('1 / V (min/mmol)')
plt.title('Lineweaver-Burk Plot')
plt.legend()

# Linear regression for Lineweaver-Burk plot
slope, intercept = np.polyfit(inv_substrate_concentration, inv_product_formation, 1)
slope_inh, intercept_inh = np.polyfit(inv_substrate_concentration, inv_product_formation_inh, 1)

x = np.linspace(0, max(inv_substrate_concentration), 100)
y = slope * x + intercept
y_inh = slope_inh * x + intercept_inh

plt.plot(x, y)
plt.plot(x, y_inh)

plt.show()

# Calculate Vmax and Km
Vmax = 1 / intercept
Km = slope / intercept

Vmax_inh = 1 / intercept_inh
Km_inh = slope_inh / intercept_inh

print("Lineweaver-Burk Vmax:", round(Vmax, 3), "mmol/min")
print("Lineweaver-Burk Km:", round(Km, 3), "mmol")

print("Lineweaver-Burk with inhibition Vmax:", round(Vmax_inh, 3), "mmol/min")
print("Lineweaver-Burk with inhibition Km:", round(Km_inh, 3), "mmol")

# V - V/[S] (Eadie-Hofstee equation)
V_div_S = product_formation / substrate_concentration
V_div_S_inh = product_formation_with_inhibition / substrate_concentration

plt.plot(V_div_S, product_formation, 'o', label="Eadie-Hofstee")
plt.plot(V_div_S_inh, product_formation_with_inhibition, 'o', label="Eadie-Hofstee with inhibition")

plt.xlabel('V/[S] (min^(-1))')
plt.ylabel('V (mmol/min)')
plt.title('Eadie-Hofstee Plot')
plt.legend()

# Linear regression for Eadie-Hofstee plot
slope, intercept = np.polyfit(V_div_S, product_formation, 1)
x = np.linspace(min(V_div_S), max(V_div_S))
y = slope * x + intercept
plt.plot(x, y)

slope_inh, intercept_inh = np.polyfit(V_div_S_inh, product_formation_with_inhibition, 1)
x_inh = np.linspace(min(V_div_S_inh), max(V_div_S_inh))
y_inh = slope_inh * x_inh + intercept_inh
plt.plot(x_inh, y_inh)

plt.show()

# Calculate Vmax and Km
Vmax = intercept
Km = slope

Vmax_inh = intercept_inh
Km_inh = slope_inh

print("Eadie-Hofstee Vmax:", round(Vmax, 3), "mmol/min")
print("Eadie-Hofstee Km:", round(-Km, 3), "mmol")

print("Eadie-Hofstee with inhibition Vmax:", round(Vmax_inh, 3), "mmol/min")
print("Eadie-Hofstee with inhibition Km:", round(-Km_inh, 3), "mmol")
