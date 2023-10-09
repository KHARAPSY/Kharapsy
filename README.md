# Kharapsy

An ongoing project to develop a personal AI assistant, showcasing various functionalities from web scraping to natural language processing.

## Overview

This project is built step-by-step, with regular updates. Its purpose is to demonstrate development skills and the application of AI techniques in real-world scenarios. The project utilizes Docker to guarantee consistent behavior across different environments.

## Setup and Installation

### Prerequisites

- Docker
- Git

### Clone the Repository

```bash
git clone https://github.com/AcebqAce/Kharapsy.git
cd Kharapsy

```

### Building the Docker Image

Navigate to the project directory and build the Docker image:

```bash
docker build -t kharapsy .

```

### Running the AI Assistant

After building the Docker image, run the application with:

```bash
docker run kharapsy

```

### Project Structure

    src/: Contains the primary source code of the AI assistant.
    requirements.txt: Enumerates the Python packages necessary for the application.
    Dockerfile: Holds instructions for Docker to package the application inside a container.

### Future Enhancements

This project is continuously evolving. Plans for future enhancements include:

    Web scraping for gathering data.
    Natural language processing for understanding user inputs and generating user-friendly responses.
    Integration with external APIs to provide extended functionalities.


### Contributing

Though Kharapsy is primarily a personal endeavor, feedback and suggestions are always appreciated. Feel free to open an issue or submit a pull request.


### License

MIT License
