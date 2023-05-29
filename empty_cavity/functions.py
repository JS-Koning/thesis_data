import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def find_fwhm(frequency, powerreflection):
    R0 = np.min(powerreflection)
    f0 = frequency[np.argmin(powerreflection)]
    freq_ind_min = find_nearest(powerreflection[:np.argmin(powerreflection)], (1 + R0) / 2)
    freq_ind_plus = find_nearest(powerreflection[np.argmin(powerreflection):], (1 + R0) / 2) + np.argmin(powerreflection)
    fwhm = frequency[freq_ind_plus] - frequency[freq_ind_min]
    return freq_ind_min, freq_ind_plus,  fwhm

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def conductance(conductivity, thickness=2.5*10**(-7)):

    a = 22.86 * 10 ** (-3)
    b = 10.16 * 10 ** (-3)
    G = conductivity * a * thickness / b
    return G

def find_q_factor_bw(cavity_cell, freq_array, res_freq=8.5):
    fwhm = prepare_qfactor(cavity_cell, freq_array, res_freq)[0]
    res_freq = freq_array[np.argmin(cavity_cell)]
    qfactor = res_freq/fwhm
    return qfactor

def prepare_qfactor(cavity_cell, freq_array, res_freq=8.5):
    # please select an approximation for the resonance frequency, for
    # a sample 8.5 will always be okay

    # remove second res peak
    leftloc = find_nearest(freq_array, res_freq-0.1)
    rightloc = find_nearest(freq_array, res_freq+0.1)
    freqs = freq_array[leftloc:rightloc]
    pwr = cavity_cell[leftloc:rightloc]
    # interpolate the values for better calculations
    freq_inp = np.linspace(freqs[0], freqs[-1], 100000)
    pwr_inp = np.interp(freq_inp, freqs, pwr)
    fwhm_pwr = find_fwhm(freq_inp, pwr_inp)
    # print(fwhm_pwr)
    # returns:
    # fullwidthhalfmaximum, freq in fwhm, powers in fwhm
    return fwhm_pwr[2], freq_inp[fwhm_pwr[0]:fwhm_pwr[1]], pwr_inp[fwhm_pwr[0]:fwhm_pwr[1]]





