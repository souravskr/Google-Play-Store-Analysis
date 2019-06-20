.PHONY: all newenv basesetup baseclean download kagglecheck bashrun

all: newenv baseclean basesetup 

newenv:
	pip install --user pipenv
	pipenv install

basesetup: baseclean
	pipenv run python3 jitter.py
	pipenv run python3 histograms.py -i ./Data/cleanData.csv -d
	pipenv run python3 post_processing.py

baseclean: download
	pipenv run python3 cleandata.py -o ./Data/cleanData.csv -i ./Data/googleplaystore.csv

download: 
	pipenv run python3 download.py -u 

kagglecheck:
	/bin/bash kagglecheck.sh

bashrun:
	/bin/bash checkfs.sh
