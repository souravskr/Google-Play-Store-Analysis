#!/bin/bash
# This script is simply designed to check for the existance of certain files and directorys

# Color setup #
red='\e[0;31m'
lred='\e[0;41m'
blue='\e[0;34m'
normal='\e[0m'
red2='\e[0;101m'
blue2='\e[0;104m'
yellbg='\e[0;43m'
green='\e[32m'
green='\e[32m'
black='\e[30m'
#---------
###############
if [ -d "./Data" ]; then
	echo -e "${green} ./Data exists ${normal}"
else
	echo -e "${red}./Data doesn't exist.${normal} Creating the directory"
	mkdir ./Data
fi

if [ -f "./Data/googleplaystore.csv" ]; then
	echo -e "${green} ./Data/googleplaystore.csv exists ${normal}"
else
	echo -e "${yellbg}${black}googleplaystore.csv was not found in ./Data directory ${normal}"
	echo -e "${yellbg}${black}copying googleplaystore.csv from ./OrigData to ./Data ${normal}"
	cp ./OrigData/googleplaystore.csv ./Data/googleplaystore.csv
fi

ls -l ./Data

echo "Beginning data cleaning process"
pipenv run python cleandata.py -o ./Data/cleanData.csv

if [[ $? ]]; then
	echo -e "${green}./Data/cleanData.csv has been properly created${normal}"
	echo "Beginning data processing"
else
	echo -e "${red}Unable to run cleanData.py. Please make sure the virtual environment has been properly set, or that the system has the required dependencies${normal}"
	exit 1
fi

pipenv run python histograms.py -i ./Data/cleanData.csv -d
if [[ $? ]]; then
	echo -e "${green}Figures and their corresponding .csv files have been generated in ./Data folder ${normal}"
	exit 0
else
	echo -e "${red}Unable to run histograms.py. Please make sure the virtual environment has been properly set, or that the system has the required dependencies${normal}"
fi

pipenv run python post_processing.py
if [[ $? ]]; then
	echo -e "${green}Post-Processing done and figures saved in ./Data folder ${normal}"
	exit 0
else
	echo -e "${red}Unable to run post_processing.py. Please make sure the virtual environment has been properly set, or that the system has the required dependencies${normal}"
fi
