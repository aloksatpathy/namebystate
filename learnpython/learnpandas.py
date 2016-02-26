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


###Pandas I/O csv
df3=pd.read_csv(r"C:\Users\Alok Satpathy\Desktop\state\namebystate\namebystate\learnpython\testdata.csv")
print(df3.head())

df3.set_index("Date", inplace=True)
df3.to_csv("newcsv2.csv")

df4=pd.read_csv("newcsv2.csv", index_col=0)
print(df4.head())

df4.columns=["Austin HPI"]
print(df4.head())
df4.to_csv("newcsv3.csv")
df4.to_csv("newcsv4.csv", header=False)

df5=pd.read_csv("newcsv4.csv", names=["Date","Austin_HPI"], index_col=0)
print(df5.head())

df5.to_html("example.html")

df6=pd.read_csv("newcsv4.csv", names=["Date","Austin_HPI"])
print(df6.head())

df6.rename(columns={"Austin_HPI":"77006_HPI"}, inplace=True)
print(df6.head())