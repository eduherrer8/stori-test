SHELL=/bin/bash
ifdef WSL_DOCKER
DOCKER_COMPOSE := docker-compose.exe
else
DOCKER_COMPOSE := docker-compose
endif

setup:
	@$(DOCKER_COMPOSE) -f docker-compose-local.yml up -d;
	@aws dynamodb create-table --table-name Transactions --attribute-definitions AttributeName=transactionID,AttributeType=S AttributeName=fileDate,AttributeType=S --key-schema AttributeName=transactionID,KeyType=HASH AttributeName=fileDate,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --endpoint-url http://localhost:8000 --region us-east-1 &>/dev/null;	

start:
	sam build
	sam local start-api
