export
SHELL := /bin/bash

directory = venv

build: | $(directory)
	@echo "installing venv and python packages"
	source ./venv/bin/activate; \
	pip install -r requirements.txt; \

$(directory):
	@echo "Folder $(directory) does not exist"
	virtualenv --no-site-packages -p python3 $@

drop_index:
	curl -X DELETE "localhost:9200/potato*"

run:
	source ./venv/bin/activate; \
	python main.py

test:
	source ./venv/bin/activate; \
	python test.py

