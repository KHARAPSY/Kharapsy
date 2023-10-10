import json
import os
import random
import time

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the messages_config.json relative to the script's directory
config_path = os.path.join(current_directory, '../bin/messages_config.json')

# Load messages from configuration file
with open(config_path, 'r') as file:
    config_data = json.load(file)
    BASE_GOODBYE_MESSAGES = config_data['BASE_GOODBYE_MESSAGES']

def initialize_goodbye_messages():
    """Prepends 'Goodbye!' to each message and returns the shuffled list."""
    messages = [["Goodbye! ", message] for message in BASE_GOODBYE_MESSAGES]
    random.shuffle(messages)
    return messages

goodbye_messages = initialize_goodbye_messages()

def print_goodbye_message():
    global goodbye_messages

    # If all messages have been used, reset
    if not goodbye_messages:
        goodbye_messages = initialize_goodbye_messages()

    chosen_message = goodbye_messages.pop()  # Get and remove the last message from the list

    print(chosen_message[0])

    for i in range(3):
        time.sleep(1)
        print(".")

    time.sleep(1)
    print(chosen_message[1])


