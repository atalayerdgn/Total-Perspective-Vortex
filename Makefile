PYTHON = python3
PIP = pip
PYTEST = pytest
PWD = $(shell pwd)
VENV = venv
ARGS = 0 0
UTILS = $(PWD)/utils
TRAIN_TEST = $(PWD)/train_test
PIPELINE = $(PWD)/pipeline
HEADERS = $(PWD)/headers
IMPLEMENTATIONS = $(PWD)/implementations
PREPROCESSING = $(PWD)/preprocessing
DATA_URL = https://physionet.org/files/eegmmidb/1.0.0/

.PHONY: all install test clean train predict

all: install train predict

install:
	$(PYTHON) -m venv $(VENV)
	
	# Gerekli klasörleri kopyala
	cp -r $(HEADERS) $(PWD)/$(VENV)
	cp -r $(UTILS) $(PWD)/$(VENV)
	cp -r $(TRAIN_TEST) $(PWD)/$(VENV)
	cp -r $(PIPELINE) $(PWD)/$(VENV)
	cp -r $(IMPLEMENTATIONS) $(PWD)/$(VENV)
	cp -r $(PREPROCESSING) $(PWD)/$(VENV)
	cp requirements.txt $(PWD)/$(VENV)
	cp main.py $(PWD)/$(VENV)
	$(VENV)/bin/$(PIP) install --upgrade pip
	if [ ! -d "$(PWD)/$(VENV)/data" ]; then \
		mkdir $(PWD)/$(VENV)/data; \
		wget -r -N -c -np -nd --directory-prefix=$(PWD)/$(VENV)/data $(DATA_URL); \
	fi
	$(VENV)/bin/$(PIP) install -r $(PWD)/$(VENV)/requirements.txt

test:
	python3 main.py

clean:
	chmod +x ./clean.sh
	./clean.sh
	rm -rf $(VENV)

train:
	$(VENV)/bin/$(PYTHON) main.py $(ARGS) train

predict:
	$(VENV)/bin/$(PYTHON) main.py $(ARGS) predict

train_custom:
	$(VENV)/bin/$(PYTHON) main.py $(ARGS) train

predict_custom:
	$(VENV)/bin/$(PYTHON) main.py $(ARGS) predict
