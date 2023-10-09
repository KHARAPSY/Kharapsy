# save_messages.py
from database_handler import add_message_to_db

messages_to_save = [
    "Have a nice day!",
    "May the knowledge be with you!",
    "Wish you the best!",
    "Have a wonderful day!"
]

for message in messages_to_save:
    add_message_to_db(message)

print("Messages saved successfully!")

