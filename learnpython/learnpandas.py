import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
#Import Library Pandas
df = pd.read_csv("C:\AK.TXT")  #I am working in Windows environment
#Reading the dataset in a dataframe using Pandas
print(df.head(1))  #Print first three observations

web_state = {"Day": [1,2,3,4,5,6],
             "Visitors": [12,13,14,15,16,17],
             "Bounce_Rate": [25,26,27,28,29,30]}

df = pd.DataFrame(web_state)
print(df)

df=df.set_index("Day")
print(df.head())

print(df["Visitors"])
print(df.Visitors)

print(df[["Visitors","Bounce_Rate"]])
print(df.Visitors.tolist())


print(np.array(df[["Visitors","Bounce_Rate"]]))

df2 = pd.DataFrame(np.array(df[["Visitors","Bounce_Rate"]]))
print(df2)