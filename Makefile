clean: clean-build clean-pyc clean-pycache
  
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-pycache:
	find . -name '__pycache__' -exec rm -rf {} +

build: clean
	poetry run poetry-setup
	poetry build

upload: build
	poetry publish

patch: psetup
	bumpversion patch

minor: psetup
	bumpversion minor

major: psetup
	bumpversion major
