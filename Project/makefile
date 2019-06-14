.PHONY: all newenv basesetup baseclean bashrun download clean

all: newenv baseclean basesetup

newenv:
	pip install --user pipenv
	pipenv install

basesetup: baseclean
	pipenv run python3 histograms.py -i ./Data/cleanData.csv -d

baseclean: download
	pipenv run python3 cleandata.py -o ./Data/cleanData.csv

bashrun:
	/bin/bash checkfs.sh

download:
	pipenv run python3 download.py -u -o ./Data

clean:
	rm ./Data/*.png ./Data/data_for*
