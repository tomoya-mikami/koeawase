SAMPLE_FILE = none

.PHONY: build
build:
	docker build -t koebuta .

.PHONY: sample
sample:
	docker run -v $(PWD):/workdir --name sample --rm koebuta python sample_create.py ${SAMPLE_FILE}
