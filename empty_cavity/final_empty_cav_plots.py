import numpy as np
import matplotlib.pyplot as plt
import functions

# import experimental data and average
values = np.genfromtxt('final_empty_cav_exp.txt', delimiter=',', skip_header=1)
data = values[:, 1], values[:,3], values[:, 5]
#avg_data = (data[0] + data[1])/2
freq = values[:,0]


#import simulated data
simdata = np.genfromtxt('final_emtpy_sim.txt',  skip_header=5)

#plot both together in range up until 9.1ghz
# and do some fancy figuring
plt.figure(figsize=(10,6))
max_index_plot = functions.find_nearest(simdata[:, 0], 9.2)
qfactor_sim = functions.find_q_factor_bw(simdata[:max_index_plot,1], simdata[:max_index_plot,0], res_freq = 9) # find q factor of sim
plt.plot(simdata[:max_index_plot,0], simdata[:max_index_plot,1], label='Simulated Q=' + str(int(qfactor_sim)), color='black')#, marker='x', linestyle='none')
# measurements, measurement 3 isnt closed correctly, see second resonance peak. Ignore this
qfactor_exp = functions.find_q_factor_bw(data[1], freq, res_freq = 9)
plt.plot(freq, data[1], label='experimental Q=' + str(int(qfactor_exp)))
plt.xlim((8.75, 9.15))

plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.ylabel('Power reflection coefficient')
plt.xlabel('Frequency (GHz)')
plt.legend()
plt.savefig('final_empty_cav_powerrefl')
plt.show()