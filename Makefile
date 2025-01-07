# makefiletutorial.com

help:
	@echo "Available commands: flake, pylint, all"

all: flake pylint

flake:
	flake8 . -v

pylint:
	pylint *.py