.PHONY: newenv basesetup clean

newenv:
	pip install --user pipenv
	pipenv install

inlibraries:
	pip install -r requirements.txt

basesetup:
	python download.py -u -o ./Data
	python cleandata.py -o ./Data/cleanData.csv
	python histograms.py -i ./Data/cleanData.csv -d

clean:
	rm ./Data/*.png ./Data/data_for*

deepclean:
	rm ./Data/*

