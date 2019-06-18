### Optional arguments ###
import os
import requests
import argparse
import kaggle

odirectory = '.'
notcompressed = False

try:
    parser = argparse.ArgumentParser(description="""\
    This is a simple script to download Kaggle datasets. 
    It is important to have a kaggle account for the script to work.
    
    """, epilog="Group 1 - CMSC6950 - Memorial University of Newfoundland")
    #group = parser.add_mutually_exclusive_group()
    
    parser.add_argument("-u", "--uncompressed", action="store_true", help="Downloads the compressed files from Kaggle", default=False)
    parser.add_argument("-o", "--output", help="select the output directory for the files", default="./Data/")
    args = parser.parse_args()
    odirectory = args.output
    notcompressed = args.uncompressed
except:
    pass


if not os.path.isdir(odirectory):
    odirectory = '.'

def downloadData():
    if notcompressed:
        os.system('kaggle datasets download lava18/google-play-store-apps --unzip -p '+odirectory)
        return os.path.isfile(odirectory+'/google-play-store-apps.zip')
    else:
        os.system('kaggle datasets download lava18/google-play-store-apps -p '+odirectory)
        return os.path.isfile(odirectory+'/googleplaystore.csv')
        #!kaggle datasets download lava18/google-play-store-apps -p args.o


def checkLicense():
    if os.path.isfile('./Data/license.txt'):
        return True 
    else:
        return 'Kaggle\'s data license was not found'


if __name__ == "__main__":
    try:
        downloadData()
        
    except Exception as e:
        print(e)
