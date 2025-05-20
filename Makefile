YEARS = 2024 2023 2022
LATEST = 2025

install:
	python3 -m venv .
	bin/pip install pelican

build:
	# Build each year-specific site
	for year in $(YEARS); do \
		sed "s/{{YEAR}}/$$year/g" pelicanconf.template.py > $$year/pelicanconf.py; \
		cd $$year; \
		PYTHON=../bin/python OUTPUTDIR=../output/$$year PELICAN=../bin/pelican make html; \
		cd ..; \
	done
	# Build the latest site
	sed "s/{{YEAR}}/$(LATEST)/g" pelicanconf.template.py > latest/pelicanconf.py
	cd latest; PYTHON=../bin/python OUTPUTDIR=../output PELICAN=../bin/pelican make html; cd ..

