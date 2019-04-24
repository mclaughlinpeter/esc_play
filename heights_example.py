import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

plt.hist(heights)
plt.show()