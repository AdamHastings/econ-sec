import matplotlib.pyplot as plt
import numpy as np



X = np.linspace(0,2, 1000)


D = np.zeros(1000)
S = np.zeros(1000)



for i,x in enumerate(X):
    if x <= 1:
        D[i] = 1/x
    elif x <= 3/2:
        D[i] = 0.5/x
    else:
        D[i] = 0

N = 3

for i,x in enumerate(X):
    if x <= 1:
        S[i] = 0
    else:
        S[i] = N


# print(D)

plt.plot(X, D, label="demand")
plt.plot(X, S, label="supply")
plt.legend()
plt.ylim(0,5)
plt.savefig("equilibrium.png")

