# Name of the Docker image
IMAGE_NAME=kharapsy

# Default target to run when calling `make` with no arguments
all: build run

# Target to build the Docker image
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

# Target to run the Docker container
run:
	@echo "Running Docker container..."
	docker run -it $(IMAGE_NAME)

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
.PHONY: all build run

