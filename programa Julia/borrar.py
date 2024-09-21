import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("lanzamientos.txt",sep="\t",header=0)
plt.plot(df["100"],df["3"],label="resultado",marker="o")
plt.plot(df["100"],df["2"],label="teorico")
plt.xlabel("lanzamientos")
plt.ylabel("doble 6")
plt.legend()
plt.grid()
plt.show()