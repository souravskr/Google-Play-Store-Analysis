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
if [ -d "${HOME}/.kaggle/" ]; then
	echo -e "${green}~/.kaggle exists ${normal}"
else
	echo -e "${red}~/.kaggle doesn't exist.${normal} Creating the directory"
	mkdir ~/.kaggle
fi

if [ -f "${HOME}/.kaggle/kaggle.json" ]; then
	echo -e "${green}~/.kaggle/kaggle.json exists ${normal}"
	ls ~/.kaggle/kaggle.json
	exit 0
else
	echo -e "${yellbg}${black}kaggle.json was not found in ~/.kaggle directory ${normal}"
	echo -e "${yellbg}${black}Createing kaggle.json in ~/.kaggle directory ${normal}"
	echo '{"username":"dasaed","key":"c5a21dedc2490cbb99b57913084d0093"}' > ~/.kaggle/kaggle.json
	ls -l ~/.kaggle/kaggle.json
	chmod 600 ~/.kaggle/kaggle.json
	exit 0	
fi
