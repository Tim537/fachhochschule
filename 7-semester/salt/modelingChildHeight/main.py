import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)

generation_size = 10000

generations = np.zeros((10, generation_size))

for i in range(0, 10):
    if i == 0:
        generations[i] = rng.normal(loc=170, scale=10, size=generation_size)
    else:
        # generate 100 children
        for j in range(0,generation_size):
            # draw 2 random parents
            p1 = rng.integers(0, generation_size)
            p2 = rng.integers(0, generation_size)

            # calculate average height
            average_height = (generations[i-1][p1] + generations[i-1][p2]) / 2

            # calculate child adult height - assuming scale is also 10 - loc factor is set to 0.1 for improved model
            cah = average_height + rng.normal(loc=(0.1 * (170 - average_height)), scale=10)

            # store cah
            generations[i][j] = cah

# Plot histogram
plt.hist(generations[0], bins=np.arange(120, 231, 5), edgecolor="black")
plt.xlabel("Height (cm)")
plt.ylabel("Count")
plt.title("Generation 1")
plt.show()

# Plot histogram
plt.hist(generations[9], bins=np.arange(120, 231, 5), edgecolor="black")
plt.xlabel("Height (cm)")
plt.ylabel("Count")
plt.title("Generation 10")
plt.show()