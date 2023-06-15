import numpy as np
import matplotlib.pyplot as plt

import functions

print(functions.conductance(1))

dataset = np.genfromtxt('maximum_electric_field_along_middle.txt', skip_header=5)
conductivities = dataset[1:,0]
emax = dataset[1:,2]
emax = emax/2.4859
conductance = functions.conductance((conductivities))
plt.figure(figsize=((12,9)))
plt.plot(conductance, emax, color='black')

plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Maximum electric field strength [V/m]', fontsize=18)
plt.xlabel('Conductance [S]', fontsize=18)
#plt.title('Maximum E field along the middle of the sample', fontsize=16)
plt.xscale('log')
plt.savefig('e_field_along_middle.png')
plt.show()

print(conductivities, emax)
