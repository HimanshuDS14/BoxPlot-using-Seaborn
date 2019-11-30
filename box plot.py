import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from time import sleep


data = pd.read_csv("tips.csv")

sns.boxplot(x = data["tip"])

plt.show()

sns.boxplot(x = data["sex"] , y = data["total_bill"])
plt.show()

sns.boxplot(x = data["day"] , y = data["total_bill"])
plt.show()


sns.boxplot(x = data["day"] ,y = data["total_bill"] , hue = data["sex"])
plt.show()

sns.boxplot(x = data["day"] ,y = data["total_bill"] , hue = data["sex"])
sns.swarmplot(x = data["day"] ,y = data["total_bill"] , data = data)
plt.show()