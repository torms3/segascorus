cy:
	python setup.py build_ext --inplace

python3:
	python3 setup.py build_ext --inplace

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./*.egg-info
