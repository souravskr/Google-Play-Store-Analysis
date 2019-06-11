# Libraries to read optional parameters
import argparse
import os
# Libraries to clean the data
import numpy as np
import pandas as pd
import seaborn as sns
import datetime 
# Libraries to graph functions
import matplotlib

parser = argparse.ArgumentParser(description="""\
This is a simple script to manually clean the data from the lava18/google-play-store-apps dataset from Kaggle.
It will ONLY work with that data set. 
""", epilog="Group 1 - CMSC6950 - Memorial University of Newfoundland")
parser.add_argument("-a", "--all", action="store_true", help="Performs all the clean-up functions in this script", default=True)
parser.add_argument("-o", "--output", help="Select the output directory and file name. By default, it stores a file in the current directoy as cleanData.csv", default='cleanData.csv')
args = parser.parse_args()



def labelClean():
    """This function is designed to manually replace the spaces in the labels of the data. This will make the column selection easier
    """
    data1.columns= ['app','category','rating','reviews','size','installs','type','price','rated','genres','lastUpdated','appVer','osVer']
    print("Columns have been Renamed to:")
    print(list(data1.columns.values))

def blankClean():
    """This function is designed to fill any blank spaces with the keyword NA, so that the data is easier to process. 
    """
    #data1.AppVer = data1.AppVer.fillna('NA')
    #df['Tenant'].replace('', np.nan, inplace=True)
    data1.replace('', np.nan, inplace=True)
    data1.fillna('NA', inplace=True)
    print("Empty cells have been cleaned (i.e. assigned a value of 'NA')")
    print("Number of 'app' modified: ",data1[data1['app'] == 'NA'].shape[0])
    print("Number of 'category' modified: ",data1[data1['category'] == 'NA'].shape[0])
    print("Number of 'rating' modified: ",data1[data1['rating'] == 'NA'].shape[0])
    print("Number of 'reviews' modified: ",data1[data1['reviews'] == 'NA'].shape[0])
    print("Number of 'size' modified: ",data1[data1['size'] == 'NA'].shape[0])
    print("Number of 'installs' modified: ",data1[data1['installs'] == 'NA'].shape[0])
    #print("Number of 'type' modified: ",data1[data1['type'] == 'NA'].shape[0])
    print("Number of 'price' modified: ",data1[data1['price'] == 'NA'].shape[0])
    print("Number of 'rated' modified: ",data1[data1['rated'] == 'NA'].shape[0])
    #print("Number of 'genres' modified: ",data1[data1['genres'] == 'NA'].shape[0])
    print("Number of 'lastUpdated' modified: ",data1[data1['lastUpdated'] == 'NA'].shape[0])
    #print("Number of 'appVer' modified: ",data1[data1['appVer'] == 'NA'].shape[0])
    print("Number of 'osVer' modified: ",data1[data1['osVer'] == 'NA'].shape[0])
    

def removeRow(datarow):
    """\
    There is a row in the data set that doesn't have the commas properly set (i.e. it has 12 columns instead of 13). 
    For this reason, we decided to get rid of this single data point manually.
    In particular, we need to get rid of sample 10472, as it only has 12 columns, instead of the standard 13."""
    data1.drop(datarow, inplace=True)
    print("Sample 10472 has been removed due to an error in this particular datapoint")
    #data1.drop(data1.loc[[10472]])

def dateFormat():
    data1['lastUpdated']=pd.to_datetime(data1['lastUpdated'])
    print("lastUpdated column has been formated in date format")

def intFormat():
    data1['installs'] = data1['installs'].map(lambda x: x.rstrip('+'))
    data1['installs'] = data1['installs'].replace(',', '', regex = True)
    data1['installs'] = data1['installs'].astype(int)

    data1['price'] = data1['price'].map(lambda x: x.lstrip('$'))
    data1['price'] = data1['price'].replace(',', '', regex = True)
    data1['price'] = data1['price'].astype(float)

def remDuplicates():
    print("Number of Duplicated samples: ",data1[data1.duplicated(['app'])].shape[0])
    data1.drop_duplicates(subset=['app'], keep='first', inplace=True)
    print("Total Samples: ",data1.shape[0])
    print("Duplicate Data Samples have been succesfully removed")

def remColumns():
    """
    The category Type is already implicit in the category labeled 'price'
    The category Genre is already implicit in the category of 'category'
    The category appVer has no real significance
    """
    data1.drop(['type','appVer', 'genres'], inplace=True, axis=1)
    print("Total Columns: ",data1.shape[1])

def toFile(output):
    data1.to_csv(output, index=False)
    print("Output file ",output," has been generated")

if args.all:
    data1 = pd.read_csv('./Data/googleplaystore.csv' )
    labelClean()
    remColumns()
    removeRow(10472)
    blankClean()
    dateFormat()
    remDuplicates()
    intFormat()
    toFile(args.output)
    #print(data1.columns)
    


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
