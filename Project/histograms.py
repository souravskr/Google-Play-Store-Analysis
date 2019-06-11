
# Libraries to read optional parameters
import argparse
import os

# Libraries to clean the data
import numpy as np
import pandas as pd
import seaborn as sns
import datetime 

# Libraries to graph functions
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description="""\
IMPORTANT: Remember to run cleandata.py before running this script. It will not work otherwise.
This programs is designed to generate basic 
""", epilog="Group 1 - CMSC6950 - Memorial University of Newfoundland")
parser.add_argument("-a", "--all", action="store_true", help="Performs all the clean-up functions in this script", default=True)
parser.add_argument("-i", "--input", help="Select the output directory and file name. By default, it stores a file in the current directoy as cleanData.csv", default='cleanData.csv')
args = parser.parse_args()

inputFile = args.input

basicData = pd.read_csv(inputFile)

print(basicData)
    


# Troubleshooting notes
# print(data1.columns) # had a repeated index label

###data1.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
###data1.drop(data1[data1.count(axis=1) < 13],inplace=True)
#data2 = pd.DataFrame()
#data2 =  data1[data1.count(axis=1) < 13 ]
###print(data2)
#print(data1.shape)
#print(data2.shape)
#data3 = data1.count(axis=1)
#print(data3.count())
###data1['Last Updated'] = df.date.apply( lambda x: pd.to_datetime(x).strftime('%m/%d/%Y')[0] )

# This is a test comment

# This is another test comment !!!
