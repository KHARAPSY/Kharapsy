# database_handler.py
import mysql.connector

# Database configurations
DB_CONFIG = {
    "host": "mysql-container",  
    # <-- This is the name of your MySQL Docker container
    "user": "root",  
    # or your chosen MySQL user
    "password": "my-secret-pw",  
    # match this to the password you set when running the MySQL container
    "database": "kharapsydb"  
    # you might need to create this database in MySQL first
}

def add_message_to_db(message):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO goodbye_messages (message) VALUES (%s)", (message,))
        conn.commit()
    except mysql.connector.errors.IntegrityError:  # This will catch duplicate messages
        print("Message already exists in the database.")
    finally:
        cursor.close()
        conn.close()

def get_all_messages_from_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("SELECT message FROM goodbye_messages")
    messages = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return messages

