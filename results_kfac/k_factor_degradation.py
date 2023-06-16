import numpy as np
import functions
import matplotlib.pyplot as plt
import scipy
import matplotlib

# I kept some of the debugging plots. They might not be important to the reader,
# But they are to me because they helped me understand what im looking at.

##set parameters
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 14
np.set_printoptions(threshold=np.inf)
#next
#np.set_printoptions(precision=15, suppress=True, formatter={'float': lambda x: format(x, '6.3E')})

#for the other file, Q11-0.5sn_dep22_50s
incidence_photons = np.array([1.79*10**9, 1.18*10**9, 3.59*10**9, 6.44*10**9, 1.29*10**10, 3.93*10**10, 6.23*10**10])
fraction_absorbed_light = np.array([0.3785, 0.3785, 0.3785, 0.3785, 0.3785, 0.3785, 0.3785])

beta_formfactor = 2.25
elementary_charge = 1.602*10**-19

# now lets put some deltaP traces in here:
delta_p_traces = np.genfromtxt('final_traces_correction.txt', skip_header=1, delimiter=',')
#delta_p_traces = np.genfromtxt('delta_p_Q10_sn02_dep22_50s.txt', skip_header=1, delimiter=',')

delta_p_time = delta_p_traces[:,0]
delta_p_y = delta_p_traces[:,1::2]
#delta_p_y = np.absolute(delta_p_y) # negative numbers are problems
# make some fancy coloring
color = plt.cm.rainbow(np.linspace(0, 1, len(delta_p_y[0,:])))


#below for 0.2sn Q10 dep 22
#incidence_photons = np.array([2.28*10**9, 8.21*10**9, 1.25*10**10, 2.5*10**10, 7.1*10**10])
#fraction_absorbed_light = np.array([1/2.827, 1/2.827, 1/2.827, 1/2.827, 1/2.827])


### START OF CODE ###


# IMPORT DATA
simdata = np.genfromtxt('final_resfreq_only_more_points.txt',  skip_header=5)#, dtype='float64')
conductivities = simdata[:,0]
conductance = functions.conductance(conductivities)
taus = simdata[:,1]
dconductance = conductance - conductance[0]
dtausdp = (taus[0]-taus)/taus[0]

#K_factor = np.zeros(len(dconductance))
#for i in range(len(K_factor)):
#    K_factor[i] = dtausdp[i]/dconductance[i]

#plt.scatter(dtausdp, K_factor)
#plt.show()

# Again, here arbitrary offset present. This is simply to only focus on numerical correct solutions
# I decided to keep some error present to highlight that there is some
# It converges after some bigger values of dR.
index_offset = 62
dconductance = dconductance[index_offset:]
dtausdp = dtausdp[index_offset:]
conductivities=conductivities[index_offset:]
taus = taus[index_offset:]
conductance = conductance[index_offset:]

print()
# START SOME PLOTTING
plt.figure(1, figsize=(12,9))

plt.plot(conductance, taus, color='black')
#plt.xscale('log')
#plt.title('Depth of the resonance peak for various conductances', fontsize=16)
plt.xlabel('Conductance [S]', fontsize=16)
plt.ylabel('R\u2080', fontsize=18)
plt.minorticks_on()
plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ticklabel_format(axis='x', style='sci', scilimits=(-5,5))
plt.savefig('R0_vs_conductance.png')

plt.show()

#dx = np.diff(taus)
#dy = np.diff(conductance)
#dRdG = dx/dy
#k_deriv = dRdG/taus[1:]
#plt.plot(taus[1:], -1*k_deriv*taus[1:])
#plt.xlabel('depth of resonance peak')
#plt.ylabel('value of k value using differentiation')
#plt.yscale('log')
#print(-1*k_deriv[functions.find_nearest(taus, 0.37)])
#plt.show()


plt.figure(2)
plt.scatter(dconductance, dtausdp)
plt.xlabel('dConductance')
plt.ylabel('dP/P_0')
#plt.xscale('log')
#plt.yscale('log')
plt.title('dConductance vs signal strength, no degradation')
# note here that we dont measure signals this strong

# first, give some k factors here
K_factor = np.zeros(len(dconductance))
for i in range(len(K_factor)):
    K_factor[i] = dtausdp[i]/dconductance[i]

plt.figure(3)
plt.scatter(dtausdp, K_factor)
print(np.argmax(K_factor))
plt.xlabel('dR/R_0')
plt.ylabel('K factor')
plt.title('k factor for various detlaPs, no deg')
plt.show()
#plt.xscale('log')
plt.figure(4)
plt.scatter(dconductance, K_factor)
plt.xlabel('dConductance')
plt.ylabel('K factor')
plt.title('dconcutance vs K factor, no degradation')
#plt.xscale('log')
plt.figure(5)
plt.scatter(taus, K_factor)
plt.xlabel('Depth of resonance peak')
plt.ylabel('K factor')
plt.title('K factor with high dark conductivities')

#interpolate values yay

taus_inp = np.linspace(min(taus), max(taus), num=1000)
K_factor_inp_func = scipy.interpolate.interp1d(taus, K_factor)
K_factor_inp = K_factor_inp_func(taus_inp)

dtausdp_inp = np.linspace(min(dtausdp), max(dtausdp), num=1000)
K_factor_inp_func_dtausdp = scipy.interpolate.interp1d(dtausdp, K_factor)
K_factor_inp_dtausdp = K_factor_inp_func_dtausdp(dtausdp_inp)


# START SOME PLOTTING

plt.figure(10, figsize=(12,9))
plt.plot(dtausdp_inp, -K_factor_inp_dtausdp, color='black') # K factor is backwards due to inp
#plt.xscale('log')
#plt.title('Signal strength versus the K factor', fontsize=16)
plt.xlabel('\u0394R/R\u2080', fontsize=16)
plt.ylabel('K', fontsize=18)
plt.minorticks_on()
plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ticklabel_format(axis='x', style='sci', scilimits=(-5,5))
plt.savefig('dR0R0_versus_K.png')

plt.show()

plt.figure(11)
plt.plot(dtausdp_inp, -1*K_factor_inp[::-1], color='black') # K factor is backwards due to inp
#plt.xscale('log')
plt.title('Signal strength versus the K factor', fontsize=16)
plt.xlabel('\u0394R/R\u2080', fontsize=16)
plt.ylabel('K', fontsize=18)
plt.minorticks_on()
plt.grid(which = 'major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which = 'minor', color='gray', linewidth=0.5, alpha=0.3)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ticklabel_format(axis='x', style='sci', scilimits=(-5,5))
plt.savefig('testing.png')

plt.show()

plt.figure(6)
plt.plot(taus_inp, K_factor_inp)
plt.xlabel('depth of resonance peak')
plt.ylabel('K factor')
plt.title('interpolated, no deg')


#plt.xscale('log')
#plt.yscale('log')

plt.figure(8)
plt.scatter(taus_inp, K_factor_inp)
plt.xlabel('depth of resonance peak')
plt.ylabel('K factor')
plt.title('interpolated, no deg')
#plt.xscale('log')
#plt.yscale('log')



#lets plot the delta gs. We're going to change all the detlags based on interpolated dtaus
taus_inp = taus_inp[::-1] #artifact due to linspace
K_factor_inp = K_factor_inp[::-1] #artifiact due to linspace
dtausdp_inp = (taus_inp[0] - taus_inp)/taus_inp[0]



dconductance_inp = dtausdp_inp/K_factor_inp
print('dtausdp')
print(dtausdp_inp)
print('dconductance_inp')
print(dconductance_inp)
print('kfacinp')
print(K_factor_inp)
k_factor_static_old = np.max(K_factor_inp)

plt.figure(9)
delta_G_traces = np.zeros(delta_p_y.shape)
for i in range(len(delta_p_y[0,:])):
    for j in range(len(delta_p_y[:,0])):
        index_correct_kfac = functions.find_nearest(delta_p_y[j,i], dtausdp_inp)
        delta_G_traces[j,i] = delta_p_y[j,i]/K_factor_inp[index_correct_kfac]
    plt.plot(delta_p_time, delta_G_traces[:,i], label="{:.2e}".format(incidence_photons[i]) + ' fixed', color=color[i])
    plt.plot(delta_p_time, delta_p_y[:,i]/k_factor_static_old, color='black', ls='--', alpha=0.5)
plt.xlabel('time [s]')
plt.ylabel('dG')
print(delta_G_traces)
plt.legend()
plt.show()
