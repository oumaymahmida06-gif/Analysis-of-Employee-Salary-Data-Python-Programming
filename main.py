# main.py

from functions import *

def show_menu():
    print("\n====== EMPLOYEE DATA ANALYSIS ======")
    print("1. Preview dataset")
    print("2. Search for 'chief'")
    print("3. Extract 2 columns")
    print("4. Clean dataset (Pandas)")
    print("5. High earners")
    print("6. Employees from 2013")
    print("7. Police job titles")
    print("8. Create Is_Manager column")
    print("9. Show summary statistics")
    print("10. Average pay per year")
    print("11. Interactive investigation")
    print("0. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        preview_dataset()

    elif choice == "2":
        search_chief()

    elif choice == "3":
        extract_two_columns()
        
    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
