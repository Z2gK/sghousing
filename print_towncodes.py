# Prints the town code and long form of town name

import pickle

fp = open("aux/towncode_dict.p", "rb")
towncodes = pickle.load(fp)
print(type(towncodes))
for key in towncodes:
    print(key + " " + towncodes[key])
