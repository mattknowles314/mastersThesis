import matplotlib.pyplot as plt
import numpy as np
import math

Z1 = []
Z2 = []
Z3 = []
for i in np.linspace(0,50):
	Z1.append(200*(1-math.exp(-0.05*i)))
	Z2.append(230*(1-math.exp(-0.05*i)))
	Z3.append(260*(1-math.exp(-0.05*i)))

plt.plot(np.linspace(0,50),Z1, label="Z0 = 200")
plt.plot(np.linspace(0,50),Z2, label="Z0 = 230")
plt.plot(np.linspace(0,50),Z3, label="Z0 = 260")
plt.title("Z(u)")
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.legend(loc="lower right")
plt.show()