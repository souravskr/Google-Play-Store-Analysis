
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
import matplotlib.colors as mcolors
import matplotlib

# Library used in the random generation of colors
import colorsys

parser = argparse.ArgumentParser(description="""\
IMPORTANT: Remember to run cleandata.py before running this script. It will not work otherwise.
This programs is designed to generate basic 
""", epilog="Group 1 - CMSC6950 - Memorial University of Newfoundland")
parser.add_argument("-i", "--input", help="Select the output directory and file name. By default, it stores a file in the current directoy as cleanData.csv", default='cleanData.csv')
args = parser.parse_args()

inputFile = args.input
basicData = pd.read_csv(inputFile)



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



def printValues():
    print("#######################################################################################")
    print(categorydf)
    print("#######################################################################################")
    print(ratingdf)
    print("#######################################################################################")
    print(reviewsdf)
    print("#######################################################################################")
    print(sizedf)
    print("#######################################################################################")
    print(installsdf)
    print("#######################################################################################")
    print(pricedf)
    print("#######################################################################################")
    print(rateddf)
    print("#######################################################################################")
    print(lastUpdateddf)
    print("#######################################################################################")
    print(osVerdf)
    print("#######################################################################################")


def graphdf(dataframe):
    print(dataframe)
    dflabel = str(dataframe.columns[0])
    dataframe.plot(x=dflabel,y='app',kind="bar")
    plt.legend().remove()
    plt.tight_layout() # adjusting the location of axes
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.savefig('./Data/'+dflabel+'_figure.png')


graphdf(categorydf)
graphdf(ratingdf)
graphdf(reviewsdf)
graphdf(sizedf)
graphdf(installsdf)
graphdf(pricedf)
graphdf(rateddf)
graphdf(lastUpdateddf)
graphdf(osVerdf)

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
    plt.show()

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

summary()
