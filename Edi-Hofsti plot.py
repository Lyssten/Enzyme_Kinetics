import numpy as np
import matplotlib.pyplot as plt

# Define the given data
substrates = ["AMP", "CMP"]
relative_vmax = [1.0, 0.1]
km_values = [(48 - 0.75, 48 + 0.75), (940 - 220, 940 + 220)]

def v_edihofsti(substrate, vmax, km, s_range):
    return [(vmax * s) / (km + s) for s in s_range]

# Create an array of substrate concentrations (S)
s_range = np.linspace(1, 1000, 100)

# Create a function to generate plots for different Km values
def generate_plots(km_values, substrate_index):
    for km_low, km_high in km_values:
        v_low = v_edihofsti(substrates[substrate_index], relative_vmax[substrate_index], km_low, s_range)
        v_high = v_edihofsti(substrates[substrate_index], relative_vmax[substrate_index], km_high, s_range)
        v_s_ratio_low = [v / s for v, s in zip(v_low, s_range)]
        v_s_ratio_high = [v / s for v, s in zip(v_high, s_range)]

        plt.plot(v_low, v_s_ratio_low, label=f"Km = {km_low} μM")
        plt.plot(v_high, v_s_ratio_high, label=f"Km = {km_high} μM")

# Generate plots for AMP
generate_plots(km_values[0:1], 0)
plt.xlabel('Reaction Rate (V) (μM/sec)')
plt.ylabel('V/[S]')
plt.title('Edi-Hofsti Plot for AMP with varying Km')
plt.legend()
plt.show()

# Generate plots for CMP
generate_plots(km_values[1:2], 1)
plt.xlabel('Reaction Rate (V) (μM/sec)')
plt.ylabel('V/[S]')
plt.title('Edi-Hofsti Plot for CMP with varying Km')
plt.legend()
plt.show()
