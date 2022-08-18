install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-test:
	pip install --upgrade pip &&\
		pip install -r requirements-test.txt

install-local:
	pip install --upgrade pip &&\
		pip install -r requirements-local.txt

test:
	python -m pytest -vv --cov=application application_test.py

format:
	black *.py

lint:
	pylint --disable=R,C main.py
	
deploy:
	echo "Deploying app"
	eb deploy flask-env

