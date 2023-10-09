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

# Phony target to ensure the commands always run, even if there's a file named "build" or "run"
.PHONY: all build run

