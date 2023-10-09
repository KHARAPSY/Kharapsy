
def main():
    print("Hello, World! Welcome to Kharapsy AI...")

    while True:
        print("\nChoose a feature to interact with:")
        print("0: Exit")
        print("1: Knowledge Base")
        print("2: Media Controller")
        print("3: Scheduler")
        print("4: Voice Recognition")

        choice = input("\nEnter your choice (0-4): ")

        if choice == "1":
            # Assuming you have a function named `start_knowledge_base` in `knowledge_base.py`
            from knowledge_base import start_knowledge_base
            start_knowledge_base()
        elif choice == "2":
            # Assuming you have a function named `start_media_controller` in `media_controller.py`
            from media_controller import start_media_controller
            start_media_controller()
        elif choice == "3":
            # Assuming you have a function named `start_scheduler` in `scheduler.py`
            from scheduler import start_scheduler
            start_scheduler()
        elif choice == "4":
            # Assuming you have a function named `start_voice_recognition` in `voice_recognition.py`
            from voice_recognition import start_voice_recognition
            start_voice_recognition()
        elif choice == "0":
            from goodbye_module import print_goodbye_message
            print_goodbye_message()
            break
        else:
            print("Invalid choice. Please select a number between 0 and 4.")

if __name__ == "__main__":
    main()

