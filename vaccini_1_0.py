import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("dati_vaccini.csv")

data2 = data[["dosi_somministrate", "nome_area"]]

print (data2)

data2.plot(kind="bar", x="nome_area", y="dosi_somministrate", figsize=(15, 8))
plt.show()
