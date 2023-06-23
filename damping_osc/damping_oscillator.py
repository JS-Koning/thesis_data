import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

R = 2.0
L = 1.0
C = 0.5

def rlc_circuit(y, t, R, L, C):
    # Unpack the variables
    x, dx = y

    # Calculate the derivatives
    d2x = (-R * dx - x / (L * C)) / L

    # Return the derivatives
    return [dx, d2x]


# IC NOW These aren't perfect but convey the message. I couldn't find a nice image showing the response
# So i just made them myself.
initial_conditions = [(0.0, 0.5), (0.0, 2.0), (0.0, 1.0)]  # (x0, dx0)
t = np.linspace(0, 10, 1000)

# ODEINT
solutions = []
damping_values = [2.0, 0.5, 1.0]  # Damping coefficients for overdamped, underdamped, and critically damped
for ic, damping in zip(initial_conditions, damping_values):
    sol = odeint(rlc_circuit, ic, t, args=(R, L, C * damping))
    solutions.append(sol[:, 0])

# Plot the solutions
plt.figure(figsize=(12, 9))
#plt.title("Response of a unit pulse of an RLC circuit dependent on damping", fontsize=16)
plt.xlabel("Time", fontsize=18)
plt.ylabel("Voltage", fontsize=18)
plt.grid(which='major', color='black', linewidth=0.5, alpha=0.6)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.3)
plt.minorticks_on()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# Plot
plt.plot(t, solutions[0], label="Overdamped")
plt.plot(t, solutions[1], label="Underdamped")
plt.plot(t, solutions[2], label="Critically Damped")

plt.legend(prop={'size' : 20})
plt.savefig('final_thesis_discussion_response_of_RLC_circuit.png')
plt.show()
