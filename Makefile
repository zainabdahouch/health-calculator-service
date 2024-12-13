include .env
export

.PHONY: init run build test test-api run-container all

init:
	@echo "Creation d'un environnement virtuel..." 
	python3 -m venv .venv ; \
	echo "activer environnement virtuel..." ; \
	. .venv/bin/activate && \
	echo "Installer les librairies..." && \
	pip install -r requirements.txt

activate:
	. .venv/bin/activate

run:
	@echo "Running the Flask app..." &&\
	. .venv/bin/activate &&\
	python3 app.py

test:
	@echo "Running tests..."
	. .venv/bin/activate &&\
	python -m unittest test.py


test-api: 
	@echo "Test API..."
	. .venv/bin/activate &&\
	python3 test-api.py

build: activate
	@echo "Building the Docker image..."
	. .venv/bin/activate &&\
	docker build -t $(IMAGE_NAME) .


run-container:
	@echo "Run Image..."
	. .venv/bin/activate &&\
	docker run -d -p $(PORT):5000 $(IMAGE_NAME)

all: init run test test-api build run-container



