

default:
	cat ./Makefile

clean: clean-build clean-pyc
	rm -fr htmlcov/

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

twine:
	twine upload ./dist/*

release: dist twine
