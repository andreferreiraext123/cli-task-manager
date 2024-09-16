from functions import show_menu, show_tasks, add_task, delete_task, clear_screen, initialize_db

def main():
    initialize_db()  # Ensure the database and table are created
    while True:
        show_menu()  # Show the menu

        try:
            choice = int(input("Enter an option (1-5): "))  # Get user choice
        except ValueError:
            print("Error:\nJust input numbers from 1 to 5")
            continue  # Restart the loop

        if choice == 1:
            show_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            clear_screen()
        elif choice == 5:
            print("\n----Program Closing----")
            break  # Exit the loop
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
