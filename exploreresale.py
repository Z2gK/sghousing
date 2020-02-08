import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Basic resale data exploration")
parser.add_argument("-b", "--blk", type=str, help="Block number", default="510")
parser.add_argument("-s", "--street", type=str, help="Street name", default="ANG MO KIO AVE 8")
args = parser.parse_args()

period1fname = "resale-flat-prices-based-on-approval-date-1990-1999.csv"
period2fname = "resale-flat-prices-based-on-approval-date-2000-feb-2012.csv"
period3fname = "resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv"
period4fname = "resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv"
period5fname = "resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"

filter_streetname = args.street
filter_blk = args.blk

# Look at various periods
dfp5 = pd.read_csv("data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv")
dfp5_fil = dfp5[(dfp5.street_name == filter_streetname) & (dfp5.block == filter_blk)]


dfp4 = pd.read_csv("data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv")
dfp4_fil = dfp4[(dfp4.street_name == filter_streetname) & (dfp4.block == filter_blk)]

dfp3 = pd.read_csv("data/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv")
dfp3_fil = dfp3[(dfp3.street_name == filter_streetname) & (dfp3.block == filter_blk)]

dfp2 = pd.read_csv("data/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv")
dfp2_fil = dfp2[(dfp2.street_name == filter_streetname) & (dfp2.block == filter_blk)]


print("Number of sales during the period 2017- : {}".format(dfp5_fil.shape[0]))
print("Number of sales during the period 2015-2017 : {}".format(dfp4_fil.shape[0]))
print("Number of sales during the period mar 2012 - 2014 : {}".format(dfp3_fil.shape[0]))
print("Number of sales during the period 2000 - feb 2012 : {}".format(dfp3_fil.shape[0]))

