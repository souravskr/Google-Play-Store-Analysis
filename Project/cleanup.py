import kaggle
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import datetime 

data1 = pd.read_csv('./Data/googleplaystore.csv' )
data1.columns= ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Rating','Genres','LastUpdated','AppVer','OSVer']

data1.AppVer = data1.AppVer.fillna('Unknown')

print("""\
There is a row in the data set that doesn't have the commas properly set (i.e. it has 12 columns instead of 13).
For this reason, we decided to get rid of this single data point manually""")
data1.drop(10472, inplace=True)
#data1.drop(data1.loc[[10472]])
data1['LastUpdated']=pd.to_datetime(data1['LastUpdated'])
print(data1)




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



# This is another test comment !!!
