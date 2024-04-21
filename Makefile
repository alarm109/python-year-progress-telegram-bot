APPLICATION_NAME ?= year-progress-telegram-bot

build:
	docker build --tag ${APPLICATION_NAME} .

run: 
	docker run --name ${APPLICATION_NAME} -d ${APPLICATION_NAME}

stop:
	docker stop ${APPLICATION_NAME}

remove:
	docker rm ${APPLICATION_NAME}