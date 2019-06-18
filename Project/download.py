### Optional arguments ###
import os
import requests
import argparse
import kaggle
parser = argparse.ArgumentParser(description="""\
This is a simple script to download Kaggle datasets. 
It is important to have a kaggle account for the script to work.

""", epilog="Group 1 - CMSC6950 - Memorial University of Newfoundland")
#group = parser.add_mutually_exclusive_group()


parser.add_argument("-u", "--uncompressed", action="store_true", help="Downloads the compressed files from Kaggle")
parser.add_argument("-o", "--output", help="select the output directory for the files", default="./Data/")
args = parser.parse_args()
odirectory = args.output

if not os.path.isdir(odirectory):
    odirectory = '.'

if args.uncompressed:
    os.system('kaggle datasets download lava18/google-play-store-apps --unzip -p '+odirectory)
else:
    os.system('kaggle datasets download lava18/google-play-store-apps -p '+odirectory)
    #!kaggle datasets download lava18/google-play-store-apps -p args.o

