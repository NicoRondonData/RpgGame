
APP_NAME=app


## Commands local
.PHONY: lint.local
lint.local:
	pre-commit run --all-files

.PHONY: test.local
test.local:
	./test.sh

.PHONY: run.local
run.local:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

## Build images
.PHONY: build.base
build.base:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-base . --target base


.PHONY: build.linters
build.linters:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-linters . --target linters


.PHONY: build.tests
build.tests:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-tests . --target tests


.PHONY: build.dev
build:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-dev . --target development

## Commands with Docker
.PHONY: lint.docker
lint:
	docker run --rm --name $(APP_NAME)-linters $(APP_NAME)-linters:latest

.PHONY: test.docker
test:
	-@docker rm -f $(APP_NAME)-tests 2> /dev/null
	docker run --name $(APP_NAME)-tests $(APP_NAME)-tests:latest
	docker cp $(APP_NAME)-tests:/app/reports .
	docker rm -f $(APP_NAME)-tests

.PHONY: run
run:
	-@docker rm -f $(APP_NAME)-dev 2> /dev/null
	docker run --env-file=.env -d -p 8000:8000 --name $(APP_NAME)-dev -v $(PWD):/app $(APP_NAME)-dev

.PHONY: run
echo.run:
	@echo "docker run --env-file=.env -d -p 8000:8000 --name $(APP_NAME)-dev -v $(PWD):/app $(APP_NAME)-dev"

run.bash:
	-@docker rm -f $(APP_NAME)-dev 2> /dev/null
	docker run --env-file=.env -dt -p 8000:8000 --name $(APP_NAME)-dev -v $(PWD):/app $(APP_NAME)-dev bash


## Delete image
.PHONY: rmi
rmi.base:
	docker rmi -f $(APP_NAME)-base

.PHONY: rmi
rmi.linters:
	docker rmi -f $(APP_NAME)-linters

.PHONY: rmi.tests
rmi.tests:
	docker rmi -f $(APP_NAME)-tests

.PHONY: rmi
rmi:
	docker rmi -f $(APP_NAME)-dev

.PHONY: rmi.prod
rmi.prod:
	docker rmi -f $(APP_NAME)

## Delete container
.PHONY: rmi
rm:
	docker rm -f $(APP_NAME)-dev

.PHONY: rmi.base
rm.base:
	docker rm -f $(APP_NAME)-base




