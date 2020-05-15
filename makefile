SAMPLE_FILE = none
TRAINING = none
SAMPLE = none

.PHONY: build
build:
	docker build -t koebuta .

.PHONY: similarity
similarity:
	docker run -v $(PWD):/workdir --name similarity --rm koebuta python similarity.py ${TRAINING} ${SAMPLE} 
