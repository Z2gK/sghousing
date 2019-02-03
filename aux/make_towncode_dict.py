# This utility creates a dictionary that maps the town abbreviation to the town name in long form
# E.g. towncode_dict['AMK'] maps to "ANG MO KIO"
# This dictionary will be stored in a pickle file towncode_dict
# The mapping is provided in the metadata file metadata-hdb-property-information.txt
# in text format, which we copy and paste here for now and assign to a string
# The data is obtained from https://data.gov.sg/dataset/hdb-property-information

import pickle
towncode_string = """          - 'AMK - ANG MO KIO'
          - 'BB - BUKIT BATOK'
          - 'BD - BEDOK'
          - 'BH - BISHAN'
          - 'BM - BUKIT MERAH'
          - 'BP - BUKIT PANJANG'
          - 'BT - BUKIT TIMAH'
          - 'CCK - CHOA CHU KANG'
          - 'CL - CLEMENTI'
          - 'CT - CENTRAL AREA'
          - 'GL - GEYLANG'
          - 'HG - HOUGANG'
          - 'JE - JURONG EAST'
          - 'JW - JURONG WEST'
          - 'KWN - KALLANG/WHAMPOA'
          - 'MP - MARINE PARADE'
          - 'PG - PUNGGOL'
          - 'PRC - PASIR RIS'
          - 'QT - QUEENSTOWN'
          - 'SB - SEMBAWANG'
          - 'SGN - SERANGOON'
          - 'SK - SENGKANG'
          - 'TAP - TAMPINES'
          - 'TG - TENGAH'
          - 'TP - TOA PAYOH'
          - 'WL - WOODLANDS'
          - 'YS - YISHUN'"""
towncode_dict = {}
# print(towncode_string)
for line in towncode_string.split("\n"):
    keyval = line.split("'")[1].split("-")
    towncode_dict[keyval[0].strip()] = keyval[1].strip()

pickle.dump(towncode_dict,open('towncode_dict.p','wb'))
print(towncode_dict)
