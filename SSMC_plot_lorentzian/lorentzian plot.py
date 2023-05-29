import numpy as np
import matplotlib.pyplot as plt


# Lorentzian function/variant
def lorentzian(x, x0, gamma, A):
    return 1 - (A / ((x - x0)**2 + (gamma/2)**2))



x0 = 8.55
gamma = 0.2  # width changes
A = 0.0035   # just works

# Generate curves, arbitrary, but works
x = np.linspace(8, 9, 1000)
y_0 = lorentzian(x, x0, gamma, A)
y_1 = lorentzian(x, x0-0.1, gamma, A)
y_2 = lorentzian(x, x0, gamma, A+0.0005)
# Plot
plt.figure(figsize=(12, 9))
plt.plot(x, y_0, color='black')
plt.plot(x, y_1, color='black', ls='--')
plt.plot(x, y_2, color='black', ls='--')
plt.xlabel('Frequency [GHz]', fontsize=18)
plt.ylabel('Power reflection coefficient', fontsize=18)
plt.minorticks_on()
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.5)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Influence of material properties on the sample', fontsize=18)
plt.savefig('depth_res_freq.png')
plt.show()
