# makefiletutorial.com

help:
	@echo "Available commands: flake, pylint, test, all"

all: flake pylint test

flake:
	flake8 . -v

pylint:
	pylint *.py

test:
	pytest --cov-config=.coveragerc --cov-report=html --cov=. --cov=tasks -vs