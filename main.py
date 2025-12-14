from functions import*
def show_menu():
    print("\n====== EMPLOYEE DATA ANALYSIS ======")
    print("1. File Handling")
    print("2. Data Cleaning")
    print("3. Subsetting And Filtering")
    print("4. Create Computed Columns")
    print("5. Summary Statistics")
    print("6. Grouping & Aggregation")
    print("7. Joining")
    print("8. Interactive Investigation Script")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        File_Handling()

    elif choice == "2":
        Data_Cleaning()

    elif choice == "3":
        Subsetting_And_Filtering()

    elif choice == "4":
        Create_Computed_Columns()

    elif choice == "5":
        Summary_Statistics()
    
    elif choice == "6":
        Grouping_And_Aggregation()
        
    elif choice=="7":
        joining()

    elif choice=="8":
        Interactive_Investigation()

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
