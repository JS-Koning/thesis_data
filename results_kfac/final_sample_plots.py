import numpy as np
import functions
import matplotlib.pyplot as plt



""" Start of code """
simdata = np.genfromtxt('final_samp_sim.txt',  skip_header=5)
frequencies = simdata[:,0]
cond = simdata[:,0]     # simulated conductivities
power_refl = simdata[:, 1:]
frequencies = np.arange(8.47, 8.55, 0.0005) # really really bad hard coding. But im stressed and running out of time

plt.figure(figsize=(10,6))
linestyles = ['dashed', 'solid', 'solid']
zorder = np.array([10, 2, 2])
for i in range(len(cond)):
    qfactor = functions.find_q_factor_bw(power_refl[i, :], frequencies, res_freq=8.5)
    plt.plot(frequencies, power_refl[i, :], label=str('{:.2e}'.format(functions.conductance(cond[i]))) + ' [S]', ls=linestyles[i], zorder=zorder[i])




plt.xlim((8.47, 8.53))

plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.ylabel('Power reflection coefficient')
plt.xlabel('Frequency (GHz)')
plt.legend()
plt.savefig('final_sample_cav_powerrefl_zoomedout')
plt.show()

# This is horrible coding, but I kind of just need to make it work for plotting purposes

plt.figure(figsize=(10,6))
linestyles = ['dashed', 'solid', 'solid']
zorder = np.array([10, 2, 2])
for i in range(len(cond)):
    qfactor = functions.find_q_factor_bw(power_refl[i, :], frequencies, res_freq=8.5)
    plt.plot(frequencies, power_refl[i, :], label=str('{:.2e}'.format(functions.conductance(cond[i]))) + ' [S]', ls=linestyles[i], zorder=zorder[i])
    print(qfactor)


#max_index_plot = functions.find_nearest(power_refl, 8.8)
#qfactor_sim = functions.find_q_factor_bw(power_refl[:max_index_plot,1], simdata[:max_index_plot,0], res_freq = 8.5) # find q factor of sim
#plt.plot(simdata[:max_index_plot,0], simdata[:max_index_plot,1], label='Simulated Q=' + str(int(qfactor_sim)), color='black')#, marker='x', linestyle='none')
# measurements, measurement 3 isnt closed correctly, see second resonance peak. Ignore this
#qfactor_exp = functions.find_q_factor_bw(data[1], freq, res_freq = 9)
#plt.plot(freq, data[1], label='experimental Q=' + str(int(qfactor_exp)))


plt.xlim((8.496, 8.506))
plt.ylim([0.63, 0.72])

plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.ylabel('Power reflection coefficient')
plt.xlabel('Frequency (GHz)')
plt.legend()
plt.savefig('final_sample_cav_powerrefl_zoomedin')
plt.show()