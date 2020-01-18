# Load data and maybe perform some initial analysis
# list estates that are likely to reach MOP this year (2020), i.e. they need to be built around 2015 or 2014
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/hdb-property-information.csv')
easttowns = set(["BD", "GL", "KWN", "MP"])
df_fil = df[df["bldg_contract_town"].isin(easttowns)].copy()

import pickle
import datetime

fp = open("aux/towncode_dict.p", "rb")
towncodes = pickle.load(fp)
towncodes2town = (lambda code: towncodes[code])

df_MOP = df_fil[(df_fil.year_completed == 2015) | (df_fil.year_completed == 2014)]
df_MOPall = df[(df_fil.year_completed == 2015) | (df_fil.year_completed == 2014)]

df_MOPnarrow = df_MOP.loc[:,["blk_no","street","max_floor_lvl","year_completed","bldg_contract_town","total_dwelling_units", "3room_sold","4room_sold","5room_sold","exec_sold","multigen_sold","studio_apartment_sold"]]
df_MOPnarrow.to_csv("MOP-east-narrow.csv", index=False)

df_MOPallnarrow = df_MOPall.loc[:,["blk_no","street","max_floor_lvl","year_completed","bldg_contract_town","total_dwelling_units", "3room_sold","4room_sold","5room_sold","exec_sold","multigen_sold","studio_apartment_sold"]]
df_MOPallnarrow.to_csv("MOP-all-narrow.csv", index=False)
