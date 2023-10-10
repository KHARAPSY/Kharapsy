import requests
from bs4 import BeautifulSoup
import mysql.connector
import json
import os

# Adjust the path
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "db_config.json")

def load_db_config():
    with open(CONFIG_PATH, "r") as file:
        config = json.load(file)
    return config

def save_to_mysql(data):
    config = load_db_config()
    conn = None
    # MySQL connection setup
    try:
        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            title VARCHAR(255),
            company VARCHAR(255)
        )
        """)

        # Insert data
        for row in data:
            cursor.execute("""
            INSERT INTO contacts (name, title, company)
            VALUES (%s, %s, %s)
            """, (row[0], row[1], row[2]))

        conn.commit()

        print("Data saved to MySQL database")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn:
            cursor.close()
            conn.close()

def scraper_configuration():
    try:  
        # Capture scraping configuration
        url = input("Enter the URL: ")  
        
        result_tag = input("Enter the result tag (e.g., div): ")
        result_class = input("Enter the result class: ")

        name_tag = input("Enter the name tag (e.g., h1): ")
        name_class = input("Enter the class for name: ")

        title_tag = input("Enter the title tag (e.g., div): ")
        title_class = input("Enter the class for title: ")

        company_tag = input("Enter the company tag (e.g., h1): ")
        company_class = input("Enter the class for company: ")


        # Execute scraping based on the provided configuration
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = []

        results = soup.find_all(result_tag, class_=result_class)

        for result in results:
            name_element = result.find_next(name_tag, class_=name_class)
            name = name_element.text.strip() if name_element else ''

            title_element = result.find_next(title_tag, class_=title_class)
            title = title_element.text.strip() if title_element else ''

            company_element = result.find_next(company_tag, class_=company_class)
            company = company_element.text.strip() if company_element else ''

            data.append([name, title, company])

        if data:
            save_to_mysql(data)
            print("Data save in database.")
        else:
            print("No data found with the provided tags and classes.")

    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

