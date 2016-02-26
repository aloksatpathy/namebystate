import Quandl
import pandas as pd

# api_key = open("quandlapikey.txt","r").read()
# df = Quandl.get("FMAC/HPI_AK", authtoken=api_key)
# print(df.head())

#html read
fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")

#this is a list
#print(fiddy_states)

#this is a dataframe
# print(fiddy_states[0])

#this is a column
# print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:    #[1:] is to ignore the column header that is Abbreviation
    print(str(abbv))


### combining dataframes - concatenating and appending dataframes
df1 = pd.DataFrame({"HPI":[80,85,88,85],
                    "Int_rate":[2,3,2,2],
                    "US_GDP_Thousands":[50,55,65,55]},
                    index = {2001,2002,2003,2004})

df2 = pd.DataFrame({"HPI":[80,85,88,85],
                    "Int_rate":[2,3,2,2],
                    "US_GDP_Thousands":[50,55,65,55]},
                    index = {2005,2006,2007,2008})

df3 = pd.DataFrame({"HPI":[80,85,88,85],
                    "Int_rate":[2,3,2,2],
                    "Low_Tier_HPI":[50,55,65,55]},
                    index = {2001,2002,2003,2004})

concat = pd.concat([df1, df2, df3])
print(concat)

concat1 = pd.concat([df1, df2])
print(concat1)

df4 = df1.append(df2)
print(df4)

df5 = df1.append(df3)
print(df5)

s=pd.Series([81,21,51])
df6 = df1.append(s, ignore_index=True)
print(df6)

s1=pd.Series([81,21,51], index = ["HPI","Int_rate","US_GDP_Thousands"])
df7 = df1.append(s1, ignore_index=True)
print(df7)