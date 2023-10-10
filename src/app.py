from knowledge_base import start_knowledge_base
from media_controller import start_media_controller
from scheduler import start_scheduler
from voice_recognition import start_voice_recognition
from contact_scraper import scraper_configuration
from goodbye_module import print_goodbye_message

def main():
    print("Hello, World! Welcome to Kharapsy AI...")

    while True:
        print("\nChoose a feature to interact with:")
        print("0: Exit")
        print("1: Knowledge Base")
        print("2: Media Controller")
        print("3: Scheduler")
        print("4: Voice Recognition")
        print("5: Contact Scraper")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            start_knowledge_base()
        elif choice == "2":
            start_media_controller()
        elif choice == "3":
            start_scheduler()
        elif choice == "4":
            start_voice_recognition()
        elif choice == "5":
            scraper_configuration()
        elif choice == "0":
            print_goodbye_message()
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5 or 0 to exit program.")

if __name__ == "__main__":
    main()

