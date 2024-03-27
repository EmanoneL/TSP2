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

fig = plt.figure(figsize=(14, 5))
ax = fig.add_subplot()
ax.step(t_mas, N_mas)
ax.grid()

plt.title('Пуассоновский поток событий')
plt.xlabel('Время, t')
plt.ylabel('Количество деталей, N')

cell_text = [['t', 'N']] + [[str(t_mas[i]), str(N_mas[i])] for i in range(len(t_mas))]

plt.table(cellText=cell_text, loc='right')

plt.show()

