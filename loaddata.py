# Load data and maybe perform some initial analysis
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/hdb-property-information.csv')
#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df["year_completed"].head())

# Let's plot a histogram of the build-years. Each bin counts the number of blocks
# Our bins are 5-yearly

#year_completed_max = max(df["year_completed"])
#year_completed_min = min(df["year_completed"])

#bins_min = year_completed_min - year_completed_min % 5
#bins_max = year_completed_max - year_completed_max % 5 + 5

#plt.hist(df["year_completed"],bins=list(range(bins_min, bins_max+1, 5)))
#plt.title("Number of HDB blocks and their year of completion")
#plt.ylabel("Number of blocks")
#plt.xlabel("Year completed")
#plt.show()

# filter for eastie towns
# easttowns = set(["BD", "GL", "KWN", "MP", "PRC", "TAP"])
# Filtering out Pasir Ris and Tampines
easttowns = set(["BD", "GL", "KWN", "MP"])
# May want to include HG, SGN
# Create a new copy altogether and work on this from hence on
df_fil = df[df["bldg_contract_town"].isin(easttowns)].copy()
print("\nSanity check that a new data frame has been created for the chosen towns")
print(df.shape)
print(df_fil.shape)
print("==================================================")

# -------------------------------------------------
# deal with df_fil from here on
# Where are the newest flats? Especially those built in the last 25 years
# We look at 5 year bins
import pickle
import datetime

fp = open("aux/towncode_dict.p", "rb")
towncodes = pickle.load(fp)
towncodes2town = (lambda code: towncodes[code])
                  
currentyr = datetime.datetime.now().year

# puts flats in 5 year bins
df_fil["agebin"] = (currentyr - df_fil["year_completed"]) // 5

# how many new flats were built there in each 5 year range?
# a look at the past 20 years
print("\nFor the chosen towns, how many blocks of flats were built in each 5 year bin?")
for bin in range(4):
    print(df_fil[df_fil.agebin == bin].shape[0])
print("==================================================")

# how many new blocks were built in each town for the respective bins?
print("\nBlocks of flats built in each 5 year bin, grouped by town")
for bin in range(4):
    print(df_fil[df_fil.agebin == bin].groupby("bldg_contract_town")["bldg_contract_town"].count())
print("==================================================")


# What are the street names of these properties?
print("\nWhere are these properties?")
for bin in range(4):
    print("Bin: %s" % bin, end= " ")
    print(" - Displaying towns: ", end = " ")
    tcodes = df_fil[df_fil.agebin == bin]["bldg_contract_town"].unique()
    towns = list(map(towncodes2town, tcodes))
    print(towns)
    for code in tcodes:
        print(code)
        df_fil_sub = df_fil[(df_fil.agebin == bin) & (df_fil.bldg_contract_town == code)]
        print(df_fil_sub["street"].unique())
    print("")
print("==================================================")

# Why are Marine Parade estates in the list, esp in bins 1, 2 and 3? These are old estates
# Eunos Cres as well - there should not be new flats there in the past 20 years
# Possibly non-residential properties

print("Why are Marine Parade estates in the list, esp in bins 1, 2 and 3? These are old estates")
print(df_fil[(df_fil.agebin <=3) & (df_fil.bldg_contract_town == "MP")].loc[:,["residential","commercial","multistorey_carpark","precinct_pavilion"]])
print("These are multistorey carparks and precinct pavilions - should filter these out")

print("==================================================")

print("Apply the filter again and keep only those with residential flag == Y")
df_fil = df[df["bldg_contract_town"].isin(easttowns) & (df["residential"] == "Y")].copy()
print(df_fil.shape)
df_fil["agebin"] = (currentyr - df_fil["year_completed"]) // 5
print("==================================================")

# What are the street names of these properties?
print("\nWhere are these properties?")
for bin in range(4):
    print("Bin: %s" % bin, end= " ")
    print(" - Displaying towns: ", end = " ")
    tcodes = df_fil[df_fil.agebin == bin]["bldg_contract_town"].unique()
    towns = list(map(towncodes2town, tcodes))
    print(towns)
    for code in tcodes:
        print(code)
        df_fil_sub = df_fil[(df_fil.agebin == bin) & (df_fil.bldg_contract_town == code)]
        print(df_fil_sub["street"].unique())
    print("")
print("==================================================")

# Dump filtered desired data to another csv file
print("Dump these data to a csv")
df_fil[(df_fil.agebin <= 3)].to_csv("east20years.csv", index=False)

print("==================================================")
print("Select certain columns and dump to another csv file")
df1 = df_fil.loc[:,["blk_no","street","max_floor_lvl","year_completed","total_dwelling_units", "3room_sold","4room_sold","5room_sold","exec_sold","multigen_sold","studio_apartment_sold","agebin"]]
df1.to_csv("east20-narrow.csv", index=False)

#townlist = df_fil[df_fil["agebin"] == 0]["bldg_contract_town"].unique()
#for towncode in townlist:
#    print(towncodes[towncode])

# print(df_fil[df_fil["agebin"] == 0].groupby("bldg_contract_town").count())
# print(townlist)

# TODO - plot lease years remaining
# Where are all the oldest flats
# Where are all the newest flats
# load the pickle file
