.PHONY: all newenv basesetup baseclean bashrun download clean

all: newenv baseclean basesetup postprocessing

newenv:
	pip install pipenv
	pipenv install

basesetup: baseclean
	pipenv run python3 histograms.py -i ./Data/cleanData.csv -d

baseclean: download
	pipenv run python3 cleandata.py -o ./Data/cleanData.csv -i ./Data/googleplaystore.csv

postprocessing: baseclean
	pipenv run python3 post_processing.py

bashrun:
	/bin/bash checkfs.sh

download:
	pipenv run python3 download.py -u -o ./Data

