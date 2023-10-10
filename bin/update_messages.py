import json
import os
import sys

config_path = 'config/messages_config.json'

def load_messages():
    with open(config_path, 'r') as file:
        data = json.load(file)
        return data['BASE_GOODBYE_MESSAGES']

def save_messages(messages):
    with open(config_path, 'w') as file:
        json.dump({"BASE_GOODBYE_MESSAGES": messages}, file, indent=4)

def add_message(message):
    messages = load_messages()
    messages.append(message)
    save_messages(messages)

def remove_message(message):
    messages = load_messages()
    if message in messages:
        messages.remove(message)
        save_messages(messages)
    else:
        print(f"Message '{message}' not found!")

def update_message(old_message, new_message):
    messages = load_messages()
    if old_message in messages:
        index = messages.index(old_message)
        messages[index] = new_message
        save_messages(messages)
    else:
        print(f"Message '{old_message}' not found!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 update_messages.py <add/remove/update> <message> [<new_message> if updating]")
        sys.exit(1)

    operation = sys.argv[1]
    message = sys.argv[2]

    if operation == "add":
        add_message(message)
    elif operation == "remove":
        remove_message(message)
    elif operation == "update":
        if len(sys.argv) < 4:
            print("For updating, please provide the new message.")
            sys.exit(1)
        new_message = sys.argv[3]
        update_message(message, new_message)
    else:
        print(f"Unknown operation: {operation}")

