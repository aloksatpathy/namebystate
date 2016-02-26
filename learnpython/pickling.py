import pandas as pd
import Quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

###pandas pickling
api_key = open("quandlapikey.txt","r").read()

def state_list():
    fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states=state_list()
    main_df = pd.DataFrame()

    for abbv in states:    #[1:] is to ignore the column header that is Abbreviation
        query = "FMAC/HPI_"+str(abbv)
        df = Quandl.get(query, authtoken=api_key)
        df[df.columns[0]] = (df[df.columns[0]]-df[df.columns[0]][0]) / df[df.columns[0]][0] * 100.0
        df.columns=[str(abbv)]              #added this to ensure each column has a unique name

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    pickle_out = open("fiddy_states3.pickle","wb")
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = Quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df[df.columns[0]] = (df[df.columns[0]]-df[df.columns[0]][0]) / df[df.columns[0]][0] * 100.0
    return df

#grab_initial_state_data()

# pickle_in = open("fiddy_states.pickle","rb")
# HPI_data = pickle.load(pickle_in)
# print(HPI_data)


# HPI_data.to_pickle("pickle.pickle")
# HPI_data2 = pd.read_pickle("pickle.pickle")
# print(HPI_data2)

HPI_data = pd.read_pickle("fiddy_states3.pickle")

# HPI_data["TX2"]=HPI_data["TX"]*2
# print(HPI_data[["TX","TX2"]])


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

TX1yr = HPI_data["TX"].resample("A", how="ohlc")
print(TX1yr.head())

HPI_data["TX"].plot(ax=ax1, label="Monthly TX HPI")
TX1yr.plot(ax=ax1, label="Yearly TX HPI")

plt.legend(loc=4)
plt.show()

