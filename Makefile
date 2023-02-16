
install:
	python3 -m venv .
	bin/pip install pelican

build:
	cd 2022; PYTHON=../bin/python OUTPUTDIR=../output/2022 PELICAN=../bin/pelican make html
	cd latest; PYTHON=../bin/python OUTPUTDIR=../output PELICAN=../bin/pelican make html

