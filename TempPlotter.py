import pandas as pd
from matplotlib import pyplot as plt
import sys

input1 = sys.argv[1]

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["temp. inlet coil","temp. outlet coil","temp. inlet radiator","temp. outlet radiator"]

df = pd.read_csv(input1, usecols=columns)
print("Contents in csv file:\n", df)
plt.plot(df.columns[1], df.columns[2])
plt.show()
