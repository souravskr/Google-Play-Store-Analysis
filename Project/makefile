.PHONY: newenv inlibraries basesetup clean

newenv:
	virtualenv -p python3 cmsc6950_g1 && source ./bin/activate

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

