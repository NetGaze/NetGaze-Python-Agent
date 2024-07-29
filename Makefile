wheel:
	python setup.py bdist_wheel

libs:
	pip install -r requirements.txt

dev-install:
	pip install -e .