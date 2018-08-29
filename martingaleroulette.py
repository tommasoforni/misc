import numpy as np
import matplotlib.pyplot as plt
N = 100000
giocate = np.zeros(N)
profits = np.zeros(N)
for i in range(N):
    cash = 100
    posta = 1
    while cash > posta and profits[i] <= 50:
        if np.random.random() > 18./37.:
            cash = cash - posta
            posta = posta *2
        else:
            cash = cash + posta
            posta = 1
        giocate[i] += 1
        profits[i] = cash - 100
    print(i)

print(np.sum(giocate)/N)
print(np.sum(profits)/N)
plt.hist(giocate,range=(-101,200),bins=100)
plt.hist(profits,range=(-101,200),bins=100)
plt.show()
