import random
import time

# Centralized list of all possible messages.
BASE_GOODBYE_MESSAGES = [
    "Have a nice day!",
    "May the knowledge be with you!",
    "Wish you the best!",
    "Have a wonderful day!"
    # You can add more messages to this list in the future.
]

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


