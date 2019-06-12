
# Libraries to read optional parameters
import argparse
import os
import sys

# Libraries to clean the data
import numpy as np
import pandas as pd
import seaborn as sns
import datetime 

# Libraries to graph functions
from matplotlib import pyplot as plt
#import matplotlib.colors as mcolors
import matplotlib

parser = argparse.ArgumentParser(description="""\
IMPORTANT: Remember to run cleandata.py before running this script. It will not work otherwise.
This programs is designed to generate basic 
""", epilog="Group 1 - CMSC6950 - Memorial University of Newfoundland")

parser.add_argument("-i", "--input", help="Select the input directory and file name. By default, it searches for cleanData.csv in the current directoy", default='cleanData.csv')
parser.add_argument("-v", "--verbose", help="increases verbosity of the output", action="count", default=0)
parser.add_argument("-d", "--data", help="Save the figure and its corresponding data", action="store_true", default=False)
parser.add_argument("-g", "--graphs", help="Enable this option to display the graphs after the figures have been processed", action="store_true", default=False)

group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--specific", help="specify which graph you wish to regenerate. The options are: category, reviews, rating, size, installs, price, rated, lastUpdated, osVer, and summary. Using a different keyword, or not filling in an option, will not do anything.", default='ignore')
group.add_argument("-a", "--all", help="same as activating flags -v -d and -g", default=True, action="store_true")

args = parser.parse_args()

if args.all == True:
    args.data = True
    args.verbose=1
    args.graphs=True


inputFile = args.input

# print(basicData.columns)
# 'app', 'category', 'rating', 'reviews', 'size', 'installs', 'price', 'rated', 'lastUpdated', 'osVer'

#print(basicData.set_index(['app','rating']))

categorydf = pd.read_csv(inputFile).groupby('category').agg(np.size).iloc[:,0:1]
categorydf.reset_index(level=0, inplace=True)

reviewsdf = pd.read_csv(inputFile).groupby('reviews').agg(np.size).iloc[:,0:1]
reviewsdf.reset_index(level=0, inplace=True)

ratingdf = pd.read_csv(inputFile).groupby('rating').agg(np.size).iloc[:,0:1]
ratingdf.reset_index(level=0, inplace=True)

sizedf = pd.read_csv(inputFile).groupby('size').agg(np.size).iloc[:,0:1]
sizedf.reset_index(level=0, inplace=True)

installsdf = pd.read_csv(inputFile).groupby('installs').agg(np.size).iloc[:,0:1]
installsdf.reset_index(level=0, inplace=True)

pricedf = pd.read_csv(inputFile).groupby('price').agg(np.size).iloc[:,0:1]
pricedf.reset_index(level=0, inplace=True)

rateddf = pd.read_csv(inputFile).groupby('rated').agg(np.size).iloc[:,0:1]
rateddf.reset_index(level=0, inplace=True)

lastUpdateddf = pd.read_csv(inputFile).groupby('lastUpdated').agg(np.size).iloc[:,0:1]
lastUpdateddf.reset_index(level=0, inplace=True)

osVerdf = pd.read_csv(inputFile).groupby('osVer').agg(np.size).iloc[:,0:1]
osVerdf.reset_index(level=0, inplace=True)

def toFile(dataframe):
    output = './Data/data_for_'+str(dataframe.columns[0])+'_figure.csv'
    dataframe.to_csv(output, index=False)
    if args.verbose == 1:
        print("Output file ",output," has been generated")

def printdf(dataframe):
    print("#######################################################################################")
    print(dataframe)
    print("#######################################################################################")

def graphdf(dataframe):
    dflabel = str(dataframe.columns[0])
    if args.verbose == 1:
        print("Generating "+dflabel+" figure")
    dflabel = str(dataframe.columns[0])
    dataframe.plot(x=dflabel,y='app',kind="bar")
    plt.legend().remove()
    plt.tight_layout() # adjusting the location of axes
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.savefig('./Data/'+dflabel+'_figure.png')

def summary():
    """
    This function generates a histogram of the number of Apps vs. the Mentioned Categories.
    Sub-Figure 1 = Number of Apps in each category
    Sub-Figure 2 = Number of Apps that have the given rating
    Sub-Figure 3 = Number of Apps that have the given amount of Reviews
    Sub-Figure 4 = Number of Apps that are of the given amount of size
    Sub-Figure 5 = Number of Apps that have that number of installs
    Sub-Figure 6 = Number of Apps that have that given price
    Sub-Figure 7 = Number of Apps that have that given Rating Category
    Sub-Figure 8 = Number of Apps that have that were last updated on that given date
    Sub-Figure 9 = Number of Apps that have that work at least on the specified Android Version
    """
    histogram, axes = plt.subplots(3,3) # Create a figure
    
    axes[0,0].bar(categorydf['category'], categorydf['app'])
    axes[0,0].title.set_text('Categories')
    axes[0,0].set_xticklabels([])
    
    axes[0,1].bar(ratingdf['rating'], ratingdf['app'])
    axes[0,1].title.set_text('Ratings')
    axes[0,1].set_xticklabels([])
    
    axes[0,2].bar(reviewsdf['reviews'], reviewsdf['app'])
    axes[0,2].title.set_text('Reviews')
    axes[0,2].set_xticklabels([])
    
    axes[1,0].bar(sizedf['size'], sizedf['app'])
    axes[1,0].title.set_text('Size of Apps')
    axes[1,0].set_xticklabels([])
    
    axes[1,1].bar(installsdf['installs'], installsdf['app'])
    axes[1,1].title.set_text('Installs')
    axes[1,1].set_xticklabels([])
    
    axes[1,2].bar(pricedf['price'], pricedf['app'])
    axes[1,2].title.set_text('Prices')
    axes[1,2].set_xticklabels([])
    
    axes[2,0].bar(rateddf['rated'], rateddf['app'])
    axes[2,0].title.set_text('Rated')
    axes[2,0].set_xticklabels([])
    
    axes[2,1].bar(lastUpdateddf['lastUpdated'], lastUpdateddf['app'])
    axes[2,1].title.set_text('Last Updated')
    axes[2,1].set_xticklabels([])
    
    axes[2,2].bar(osVerdf['osVer'], osVerdf['app'])
    axes[2,2].title.set_text('OS Version')
    axes[2,2].set_xticklabels([])
    
    histogram.tight_layout() # adjusting the location of axes
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.savefig('./Data/Summary_figure.png')
    #plt.show()

#print(matplotlib.get_backend())
#input("Stop")

# Option 1
# QT backend
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()

# Option 2
# TkAgg backend
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())

# Option 3
# WX backend
#manager = plt.get_current_fig_manager()
#manager.frame.Maximize(True)

dfs = [categorydf, ratingdf, reviewsdf, sizedf, installsdf, pricedf, rateddf, lastUpdateddf, osVerdf ] 
saved = False
savedata = args.data

if args.specific == 'ignore':
    if args.verbose == 1:
        print('Using the '+inputFile+' file')
        print('Printing all summarized dataframes')
        for i in dfs:
            printdf(i)
            graphdf(i)
            if savedata == True:
                toFile(i)
                saved=True
        summary()
    
    else:
        for i in dfs:
            graphdf(i)
            if savedata == True:
                toFile(i)
                saved=True
        summary()

elif args.specific == 'category':
    graphdf(categorydf)

elif args.specific == 'rating':
    graphdf(ratingdf)

elif args.specific == 'reviews':
    graphdf(reviewsdf)

elif args.specific == 'size':
    graphdf(sizedf)

elif args.specific == 'installs':
    graphdf(installsdf)

elif args.specific == 'price':
    graphdf(pricedf)

elif args.specific == 'rated':
    graphdf(rateddf)

elif args.specific == 'lastUpdated':
    graphdf(lastUpdateddf)

elif args.specific == 'osVer':
    graphdf(osVerdf)

elif args.specific == 'summary':
    summary()

else:
    print('Wrong OPTION specified with the -s flag. Please select a valid option')
    print('The options are: category, reviews, rating, size, installs, price, rated, lastUpdated, osVer, and summary ')
    sys.exit(0)

if args.graphs == True:
    plt.show()
