import pandas as pd
import Quandl
import pickle

###pandas pickling
api_key = open("quandlapikey.txt","r").read()
fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")

main_df = pd.DataFrame()

print("main_df",main_df)

for abbv in fiddy_states[0][0][1:]:    #[1:] is to ignore the column header that is Abbreviation
    query = "FMAC/HPI_"+str(abbv)
    df = Quandl.get(query, authtoken=api_key)
    df.columns=[str(abbv)]

    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)


print(main_df.head())