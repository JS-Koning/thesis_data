import numpy as np
import matplotlib.pyplot as plt
import functions

# import experimental data and average
values = np.genfromtxt('final_quartz_cav_exp.txt', delimiter=',', skip_header=1)
print(values)
data = values[:, 1:-1:2]
freq = values[:,0]
data = np.delete(data, [-2], axis=1)
print(data)
print(data[:,0])
print('freq' + str(freq))


#import simulated data
simdata = np.genfromtxt('final_quartz_sim.txt',  skip_header=5)
print(simdata)
#plot both together in range up until 9.1ghz
# and do some fancy figuring
plt.figure(figsize=(10,6))
max_index_plot = functions.find_nearest(simdata[:, 0], 8.6)
qfactor_sim = functions.find_q_factor_bw(simdata[:max_index_plot,1], simdata[:max_index_plot,0], res_freq = 8.5) # find q factor of sim
plt.plot(simdata[:max_index_plot,0], simdata[:max_index_plot,1], label='Simulated Q=' + str(int(qfactor_sim)), color='black')#, marker='x', linestyle='none')
# measurements
cmap = plt.get_cmap('jet') #fancy colouring
for i in range(len(data[0,:])):
    qfactor_exp = functions.find_q_factor_bw(data[:,i], freq, res_freq = 8.5)
    if i <= 4:
        plt.plot(freq, data[:,i], label='Pristine Q=' + str(int(qfactor_exp)), color=cmap(2*i/len(data[0,:])))
    else:
        plt.plot(freq, data[:, i], label='Recycled Q=' + str(int(qfactor_exp)), color=cmap(i / len(data[0, :])))

plt.xlim((8.4, 8.6))

plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.ylabel('Power reflection coefficient')
plt.xlabel('Frequency (GHz)')
plt.legend()
plt.savefig('final_quartz_cav_powerrefl')
plt.show()