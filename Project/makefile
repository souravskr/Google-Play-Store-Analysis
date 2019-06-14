.PHONY: newenv basesetup download 

newenv:
	pip install --user pipenv
	pipenv install

inlibraries:
	pip install -r requirements.txt

basesetup: baseclean
	pipenv run python3 cleandata.py -o ./Data/cleanData.csv

baseclean: download
	pipenv run python3 python histograms.py -i ./Data/cleanData.csv -d

download:
	pipenv run python3 python download.py -u -o ./Data

clean:
	rm ./Data/*.png ./Data/data_for*

deepclean:
	rm ./Data/*

