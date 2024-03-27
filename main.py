import math
import random
import matplotlib.pyplot as plt

lamb = 8/24
Tn = 100
t=0
N=0
t_mas=[]
N_mas=[]
t_all = [i for i in range(Tn+1)]

while t <= Tn:
    r = random.random()
    tau = -1/lamb * math.log(r)
    t = t + tau
    N = N + 1

    t_mas.append(t)
    N_mas.append(N)

plt.figure(figsize=(8, 6))
plt.plot(t_mas, N_mas, color='blue')

plt.show()

