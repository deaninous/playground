import random
import matplotlib.pyplot as plt
import numpy as np

pos = 0
walk = [pos]
wp = [0]
steps = 1000
for x in range(steps):
	step = 1 if random.randint(0,1) else -1
	pos += step
	wp.append(x)
	walk.append(pos)
plt.xlabel('iterate')
plt.ylabel('dist')

plt.plot(wp, walk)
plt.show()

#np style
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
plt.plot(range(nsteps), walk)
plt.show()
