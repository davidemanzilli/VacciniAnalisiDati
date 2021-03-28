import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("dati_vaccini.csv") #apro il file da leggere

data2 = data[["dosi_somministrate", "nome_area", "dosi_consegnate"]] #creo un dataframe con i dati che mi servono 

# print (data2) #vedo a schermo il dataframe 

data2.plot(kind="bar", x="nome_area", figsize=(16, 8)) #creo il grafico 
plt.title("CONSEGNE-SOMMINISTRAZIONI")
plt.yticks([100000*k for k in range(0,31)])
plt.ylabel("INTERVALLO 0-3 MILIONI")
plt.xlabel("REGIONI")
plt.savefig("CONSEGNE-SOMMINISTRAZIONI.png")
plt.show() #mostro il grafico 
