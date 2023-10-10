# Name of the Docker image
IMAGE_NAME=kharapsy
COMPOSE_FILE=docker-compose.yml

# Default target to run when calling `make` with no arguments
all: build docker-run
clean: 
	$(docker-stop) docker-compose down

docker-build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

docker-run: up
	@echo "Running Docker container..."
	docker run -it $(IMAGE_NAME)

docker-stop:
	@echo "Stoping Docker container..."
	docker stop another-mysql-container

build:
	@echo "Building Docker services..."
	docker-compose -f $(COMPOSE_FILE) build

up: docker-build
	@echo "Starting Docker services..."
	docker-compose -f $(COMPOSE_FILE) up -d

down:
	@echo "Stopping Docker services..."
	docker-compose -f $(COMPOSE_FILE) down

logs:
	@echo "Displaying logs..."
	docker-compose -f $(COMPOSE_FILE) logs


# Target to list the Exit messages
list:
	@echo "Listing messages..."
	python3 bin/list_messages.py

# Targets to CRUD the Exit messages
add-message:
	@echo "Adding message..."
	python3 bin/update_messages.py add "$(message)"

remove-message:
	@echo "Removing message..."
	python3 bin/update_messages.py remove "$(message)"

update-message:
	@echo "Updating message..."
	python3 bin/update_messages.py update "$(old_message)" "$(new_message)"


# Phony target to ensure the commands always run, even if there's a file named "build" or "run"
.PHONY: all build up down logs list add-message remove-message update-message

