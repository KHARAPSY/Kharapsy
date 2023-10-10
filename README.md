# Kharapsy AI

Kharapsy AI is an interactive CLI application that provides various functionalities like Knowledge Base, Media Controller, Scheduler, and Voice Recognition. Dive in and explore the capabilities!

An ongoing project to develop a personal AI assistant, showcasing various functionalities from web scraping to natural language processing.

## Overview

This project is built step-by-step, with regular updates. Its purpose is to demonstrate development skills and the application of AI techniques in real-world scenarios. The project utilizes Docker to guarantee consistent behavior across different environments.

## Setup and Installation

### Prerequisites

- Ensure you have https://www.docker.com/ installed.

### Clone the Repository

```bash
git clone https://github.com/AcebqAce/Kharapsy.git
cd Kharapsy

```

### Build & Run the application

This will build a Docker image and run a container using that image.

```bash
make
```

#### CRUD the Exit messages

This will show the list of exit messages

```bash
make list
```

This will add new exit message

```bash
make add-message message="Your new message here."
```

This will remove exit message

```bash
make remove-message message="Message to be removed."
```

This will update exit message

```bash
make update-message old_message="Old message." new_message="New message."
```

## Features
- Knowledge Base: (Provide a brief description of this feature)
- Media Controller: (Provide a brief description of this feature)
- Scheduler: (Provide a brief description of this feature)
- Voice Recognition: (Provide a brief description of this feature)

## Modules
Here's a brief overview of the modules in the 'src' directory:

- app.py: The main entry point of the application.
- knowledge_base.py: (Briefly describe this module)
- media_controller.py: (Briefly describe this module)
- scheduler.py: (Briefly describe this module)
- voice_recognition.py: (Briefly describe this module)
- goodbye_module.py: Responsible for displaying randomized goodbye messages.

## Acknowledgments
Thanks to all.

