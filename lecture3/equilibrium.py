import matplotlib.pyplot as plt
import numpy as np



X = np.linspace(0,2, 1000)


D = np.zeros(1000)
S = np.zeros(1000)



for i,x in enumerate(X):
    if x <= 1:
        D[i] = 7/x
    elif x <= 3/2:
        D[i] = 5/x
    else:
        D[i] = 0

N = 6
for i,x in enumerate(X):
    if x <= 1:
        S[i] = 0
    else:
        S[i] = N

plt.clf()
plt.plot(X, D, label="demand")
plt.plot(X, S, label="supply")
plt.legend()
plt.xlabel("price")
plt.ylabel("quantity")
plt.yticks([0,2,4,6,8,10], ["", "", "", "N", "", ""])
plt.ylim(0,10)
plt.title("N > Y2/p")
plt.savefig("equilibrium1.png")

N = 4
for i,x in enumerate(X):
    if x <= 1:
        S[i] = 0
    else:
        S[i] = N

plt.clf()
plt.plot(X, D, label="demand")
plt.plot(X, S, label="supply")
plt.legend()
plt.xlabel("price")
plt.ylabel("quantity")
plt.yticks([0,2,4,6,8,10], ["", "", "N", "", "", ""])
plt.ylim(0,10)
plt.title("N = Y2/p")
plt.savefig("equilibrium2.png")

N = 2
for i,x in enumerate(X):
    if x <= 1:
        S[i] = 0
    else:
        S[i] = N

plt.clf()
plt.plot(X, D, label="demand")
plt.plot(X, S, label="supply")
plt.legend()
plt.xlabel("price")
plt.ylabel("quantity")
plt.yticks([0,2,4,6,8,10], ["", "N", "", "", "", ""])
plt.ylim(0,10)
plt.title("N < Y2/p")
plt.savefig("equilibrium3.png")




