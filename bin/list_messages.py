import json
import os

config_path = 'config/messages_config.json'

def list_messages():
    with open(config_path, 'r') as file:
        data = json.load(file)
        for message in data['BASE_GOODBYE_MESSAGES']:
            print(message)

if __name__ == "__main__":
    list_messages()

