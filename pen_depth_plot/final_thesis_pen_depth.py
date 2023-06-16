import numpy as np
import matplotlib.pyplot as plt

freq = 8.5 * 10**9 * 2 * np.pi
cond = np.logspace(-5, 3, 100)
depth = np.sqrt(2 / (freq * cond)) * 10**9

plt.figure(figsize=(12, 9))
plt.plot(cond, depth, color='black')
plt.xscale('log')
plt.yscale('log')
#plt.title('Penetration depth vs conductivity at 8.5GHz')
plt.ylabel('penetration depth [nm]', fontsize=18)
plt.xlabel('conductivity [S/m]', fontsize=18)

plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)

plt.minorticks_on()

# Manually set the locations of the minor x ticks
plt.xticks(
    np.logspace(-5, 3, 9),
    ['1e-5', '1e-4', '1e-3', '1e-2', '1e-1', '1e0', '1e1', '1e2', '1e3'],
    fontsize=14
)
plt.yticks(fontsize=14)

plt.savefig('final_thesis_penetration_depth.png')
plt.show()
