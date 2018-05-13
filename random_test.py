import random
import matplotlib.pyplot as plt
import numpy as np

print(random.random())
print(random.uniform(1,100))
print(random.randint(1,100))
print(random.choice('1234567890abcdefghij'))

sample_list = ['python', 'izm', 'com', 'random', 'sample']
random.shuffle(sample_list)
print(sample_list)

random_list = [0 for i in range(1000)]
for i in range(1000):
    random_list[random.randint(0,999)] += 1

print(random_list)
x = np.linspace(0, 1000, 1000)
y = random_list
plt.bar(x, y)
plt.show()
