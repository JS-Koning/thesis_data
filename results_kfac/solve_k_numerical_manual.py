import numpy as np
import functions
import matplotlib.pyplot as plt
import matplotlib

##set parameters
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 14
np.set_printoptions(threshold=np.inf)

# IMPORT DATA
simdata = np.genfromtxt('final_resfreq_only_more_points.txt',  skip_header=5)#, dtype='float64')
conductivities = simdata[:,0]
conductance = functions.conductance(conductivities)
taus = simdata[:,1]
dconductance = conductance - conductance[0]
dtausdp = (taus[0]-taus)/taus[0]

# offset to ignore numerical inaccuracies. Changing this value actually shows the solution
# converging to the actual solution. Might need to change some log axes to see correct representation
# I decided to keep some of the numerical errors present since imperfections are ok.
idx_off = 56

dconductance = dconductance[idx_off:]
dtausdp = dtausdp[idx_off:]
conductivities=conductivities[idx_off:]
taus = taus[idx_off:]
conductance = conductance[idx_off:]


# Calculate the value of C using the boundary condition at x0
dR0_dG = np.gradient(taus, conductance)

k = -dR0_dG/taus


# START SOME PLOTTING
plt.figure(1, figsize=(12,9))

plt.plot(taus[:-2], -k[:-2], color='black')
#plt.xscale('log')
plt.title('K factor for various reflection coefficients', fontsize=16)
plt.xlabel('R\u2080', fontsize=18)
plt.ylabel('K factor', fontsize=16)
plt.minorticks_on()
plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ticklabel_format(axis='x', style='sci')
#plt.xscale('log')
plt.savefig('R0_vs_K_factor_numerical_differentiation')

plt.show()

# NOW SOME PLOTTING FOR DRDG

plt.figure(2, figsize=(12,9))

plt.plot(taus[:-2], dR0_dG[:-2], color='black')
#plt.xscale('log')
plt.title('dR\u2080/dG for various reflection coefficients', fontsize=16)
plt.xlabel('R\u2080', fontsize=18)
plt.ylabel('dR\u2080/dG', fontsize=16)
plt.minorticks_on()
plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ticklabel_format(axis='x', style='sci')
#plt.xscale('log')
plt.savefig('R0_vs_dR0_dG')

plt.show()

# NOW SOME PLOTTING FOR R_0DRDG
# This is not presented in the thesis however. But it was something I was working on and decided to include.

plt.figure(2, figsize=(12,9))

plt.plot(taus[:-2], taus[:-2]*dR0_dG[:-2], color='black')
#plt.xscale('log')
plt.title('dR\u2080/dG for various R\u2080s', fontsize=16)
plt.xlabel('R\u2080', fontsize=18)
plt.ylabel('R\u2080*dR\u2080/dG', fontsize=16)
plt.minorticks_on()
plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ticklabel_format(axis='x', style='sci')
#plt.xscale('log')
plt.savefig('R0_vs_R_0dR0_dG')

plt.show()
