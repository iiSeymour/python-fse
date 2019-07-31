clean:
	python setup.py clean
	rm -rf _fse.* *~ pyfse.egg-info build

build:
	python setup.py develop

test: build
	python tests/fse_tests.py
