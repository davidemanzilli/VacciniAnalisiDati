import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv")

data2 = data[["percentuale_somministrazione", "nome_area",]] #creo un dataframe con i dati che mi servono 

# print (data2) #vedo a schermo il dataframe 

data2.plot(kind="bar", x="nome_area", y="percentuale_somministrazione", figsize=(16, 8), color="green") #creo il grafico 
plt.title("CONSEGNE-SOMMINISTRAZIONI-PERCENTUALE")
plt.yticks([10*k for k in range(0,11)])
plt.ylabel("IN PERCENTUALE %")
plt.xlabel("REGIONI")
plt.savefig("CONSEGNE-SOMMINISTRAZIONI-PERCENTUALE.png")
plt.show() #mostro il grafico 
