import numpy as np
import matplotlib.pyplot as plt

"""
Hi, and welcome to the giant codewall of death.
It's inefficient.
It's barely commented.
I refused to use loops.
I'm running out of time.
Deadlines are social constructs.

If you have questions what does what, chatGPT will assist you,
If even chatGPT doesn't know what I'm doing,
Send me a message.
"""


dataset = np.genfromtxt('final_thesis_100nm_deltaP.txt', skip_header=1, delimiter=',')
deltaP = dataset[:,1::2]
manual_k_fac = 64000
num_photons = 1.03 * 10**10
etamu = deltaP/(2.25*1.602*10**-19*num_photons*manual_k_fac)
time = dataset[:, 0]



# create a colormap
cmap = plt.cm.get_cmap('rainbow')

# generate an array of colors based on the deltaP values
colors = cmap(np.linspace(0, 1, len(deltaP[0,:])))
colors[-1] = np.array([0,0,0,1])
colors[0] = np.array([0,0,0,1])

labels = ['109 mW',
 '69.6 mW',
'41.8 mW',
'28.1 mW',
'16.9 mW',
'10.0 mW',
'6.65 mW',
'4.15 mW',
'1.98 mW',
'1.31 mW',
'109 mW']


# plot the deltaP traces with the colors - 100 nm only
plt.figure(figsize=(12, 9))
for i in range(len(deltaP[0,:])):
    if i ==0:
        plt.plot(time, etamu[:, i], color=colors[i], ls='solid', label=labels[i])
    elif i == len(deltaP[0,:])-1:
        plt.plot(time, etamu[:, i], color=colors[i], ls=(0,(1,1)), label=labels[i])
    else:
        plt.plot(time, etamu[:, i], color=colors[i], label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('dG/(\u03B2 I\u2080 e)', fontsize=18)
plt.xlabel('Time [S]', fontsize=18)
plt.legend(loc=4)
plt.title('Normalized TRMC traces with varying power, '+str("{:.2e}".format(num_photons))+' photons/cm\u00b2', fontsize=16)

# save and show the plot
plt.savefig('final_thesis_100nm_power_varying_trmc_zoomed_out.png')
plt.show()
# plot the deltaP traces with the colors
plt.figure(figsize=(12, 9))
for i in range(len(deltaP[0,:])):
    if i ==0:
        plt.plot(time, etamu[:, i], color=colors[i], ls='solid', label=labels[i])
    elif i == len(deltaP[0,:])-1:
        plt.plot(time, etamu[:, i], color=colors[i], ls=(0,(1,1)), label=labels[i])
    else:
        plt.plot(time, etamu[:, i], color=colors[i], label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('dG/(\u03B2 I\u2080 e)', fontsize=18)
plt.xlabel('Time [S]', fontsize=18)
plt.xlim([3*10**-8, 5*10**-7])
plt.ylim([8.5,12])
plt.legend(loc=0)
plt.title('Normalized TRMC traces with varying power, '+str("{:.2e}".format(num_photons))+' photons/cm\u00b2', fontsize=16)

# save and show the plot
plt.savefig('final_thesis_100nm_power_varying_trmc_zoomed_in.png')
plt.show()


"""
Here is where the horror starts, just copy everything and paste it below the original code
I really dont like this solution.
Changing some variables in the naming.


Adding some spaces


Intentionally left blank
"""


# do everything for second set of data as well:
dataset = np.genfromtxt('final_thesis_200nm_deltaP.txt', skip_header=1, delimiter=',')
deltaP = dataset[:,1::2]
manual_k_fac = 64000
num_photons = 1.06 * 10**10
etamu = deltaP/(2.25*1.602*10**-19*num_photons*manual_k_fac)
time = dataset[:, 0]



# create a colormap
cmap = plt.cm.get_cmap('rainbow')

# generate an array of colors based on the deltaP values
colors = cmap(np.linspace(0, 1, len(deltaP[0,:])))
colors[-1] = np.array([0,0,0,1])
colors[0] = np.array([0,0,0,1])

labels = ['108 mW',
 '69.0 mW',
'42.2 mW',
'28.1 mW',
'16.8 mW',
'10.4 mW',
'6.60 mW',
'4.13 mW',
'1.78 mW',
'1.37 mW',
'108 mW']


# plot the deltaP traces with the colors - 100 nm only
plt.figure(figsize=(12, 9))
for i in range(len(deltaP[0,:])):
    if i ==0:
        plt.plot(time, etamu[:, i], color=colors[i], ls='solid', label=labels[i])
    elif i == len(deltaP[0,:])-1:
        plt.plot(time, etamu[:, i], color=colors[i], ls=(0,(1,1)), label=labels[i])
    else:
        plt.plot(time, etamu[:, i], color=colors[i], label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('dG/(\u03B2 I\u2080 e)', fontsize=18)
plt.xlabel('Time [S]', fontsize=18)
plt.legend(loc=4)
plt.title('Normalized TRMC traces with varying power, '+str("{:.2e}".format(num_photons))+' photons/cm\u00b2', fontsize=16)

# save and show the plot
plt.savefig('final_thesis_200nm_power_varying_trmc_zoomed_out.png')
plt.show()
# plot the deltaP traces with the colors
plt.figure(figsize=(12, 9))
for i in range(len(deltaP[0,:])):
    if i ==0:
        plt.plot(time, etamu[:, i], color=colors[i], ls='solid', label=labels[i])
    elif i == len(deltaP[0,:])-1:
        plt.plot(time, etamu[:, i], color=colors[i], ls=(0,(1,1)), label=labels[i])
    else:
        plt.plot(time, etamu[:, i], color=colors[i], label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('dG/(\u03B2 I\u2080 e)', fontsize=18)
plt.xlabel('Time [S]', fontsize=18)
plt.xlim([3*10**-8, 5*10**-7])
plt.ylim([17,26])
plt.legend(loc=0)
plt.title('Normalized TRMC traces with varying power, '+str("{:.2e}".format(num_photons))+' photons/cm\u00b2', fontsize=16)

# save and show the plot
plt.savefig('final_thesis_200nm_power_varying_trmc_zoomed_in.png')
plt.show()

"""
Yes we are going to do the same thing for the SSMC in a single file.

We're not even using functions!

Adding more space to increase readability at least a tiny bit.

Bye.


"""
### SSMC - - -  NOW OVERWRITING VARIABLES, FIGHT ME
ssmcdataset = np.genfromtxt('ssmc_varying_power.txt', skip_header=1, delimiter=',')
frequencies = ssmcdataset[:,0]
ssmc = ssmcdataset[:, 1::2]

labels = ['161 mW', '147 mW', '132 mW', '117 mW', '102 mW', '89 mW', '73 mW', '60 mW', '43 mW', '32 mW', '14.50 mW', '7.160 mW', '1.548 mW', '0.839 mW']
cmap = plt.cm.get_cmap('rainbow')

colors = cmap(np.linspace(0, 1, len(ssmc[0,:])))



# plot the SSMC  with the colors
plt.figure(figsize=(12, 9))
for i in range(len(ssmc[0,:])):
    plt.plot(frequencies, ssmc[:, i], color=colors[i], ls='solid', label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Power reflection coefficient (R)', fontsize=18)
plt.xlabel('Frequency [GHz]', fontsize=18)
plt.xlim(np.min(frequencies), np.max(frequencies))
plt.legend(loc=4)
plt.title('Normalized SSMC measurements with varying power')
plt.savefig('final_thesis_SSMC_varyingpower_zoomed_out.png')
plt.show()

# plot the SSMC  with the colors zoom 1.
plt.figure(figsize=(12, 9))
for i in range(len(ssmc[0,:])):
    plt.plot(frequencies, ssmc[:, i], color=colors[i], ls='solid', label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Power reflection coefficient (R)', fontsize=18)
plt.xlabel('Frequency [GHz]', fontsize=18)
plt.xlim(9.18, 9.5)
plt.ylim(0.88, 1.13)
plt.legend(loc=1)
plt.title('Normalized SSMC measurements with varying power')
plt.savefig('final_thesis_SSMC_varyingpower_zoomed_in_dif.png')
plt.show()

#plot the SSMC with the colors zoom 2.
plt.figure(figsize=(12, 9))
for i in range(len(ssmc[0,:])):
    plt.plot(frequencies, ssmc[:, i], color=colors[i], ls='solid', label=labels[i])
# customize the plot
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Power reflection coefficient (R)', fontsize=18)
plt.xlabel('Frequency [GHz]', fontsize=18)
plt.xlim(8.475, 8.55)
plt.ylim(0.6, 1.13)
plt.legend(loc=4)
plt.title('Normalized SSMC measurements with varying power')
plt.savefig('final_thesis_SSMC_varyingpower_zoomed_in_res_8_5.png')
plt.show()

