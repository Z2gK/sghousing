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

year_completed_max = max(df["year_completed"])
year_completed_min = min(df["year_completed"])

bins_min = year_completed_min - year_completed_min % 5
bins_max = year_completed_max - year_completed_max % 5 + 5

plt.hist(df["year_completed"],bins=list(range(bins_min, bins_max+1, 5)))
plt.title("Number of HDB blocks and their year of completion")
plt.ylabel("Number of blocks")
plt.xlabel("Year completed")
plt.show()

# Where are the newest flats? Especially those built in the last 25 years
# We look at 5 year bins

import datetime
currentyr = datetime.datetime.now().year
df["agebin"] = (currentyr - df["year_completed"]) // 5
# d = { df[df["agebin"]==i]  for i in range(5)}
# df[bin == 0]["bldg_contract_town"].unique()


# TODO - plot lease years remaining
# Where are all the oldest flats
# Where are all the newest flats
# load the pickle file
