
import pandas as pd
# ------------------------------------------------------
# PART 1 - File Handling
# ------------------------------------------------------
def preview_dataset():
    with open("Data.csv", "r") as f:
        for i in range(5):
            print(f.readline())

def search_chief():
    with open("Data.csv", "r") as f:
        line_number=0
        found=False
        for line in f:
            line_number+=1
            if "chief" in line.lower():
                print("First occurrence found!")
                print("Line number:", line_number)
                print("Line content:")
                print(line.strip())
                found = True
                break
        if not found:
            print("The word 'chief' was not found in the file.")

def extract_two_columns():
    with open("Data.csv", "r") as f:
        header = f.readline().strip().split(",")

        print("\nAvailable columns:")
        for i in range(len(header)):
            print(i, "-", header[i])

        valid=False
        while not valid:
            column1 = int(input("Enter the index of the first column (starting from 0): "))
            column2 = int(input("Enter the index of the second column (starting from 0): "))
            if column1 < 0 or column1 >= len(header) or column2 < 0 or column2 >= len(header):
                print("Invalid column indices. Please try again.")
            else:
                valid=True

        rows=int(input("Enter the number of rows to extract : "))   

        print(f"\nExtracted columns: {header[column1]} | {header[column2]}")
        row_count = 0
        for line in f:
            columns = line.strip().split(",")

            if len(columns) > column1 and len(columns) > column2:
                print(columns[column1], "|", columns[column2])
                row_count += 1
            if row_count == int(rows):
                break

def File_Handling():
    while True:
        print("   === File Handling ===   ")
        print("1. Preview first 5 rows of the dataset.")
        print("2. Search for “chief” in the CSV.")
        print("3. Extract manually 2 columns.")
        print("0. Exit.")
        choice = input("Enter your choice: ")
        if choice=='1':
            preview_dataset()
        elif choice =='2' : 
            search_chief()
        elif choice=='3': 
            extract_two_columns()
        elif choice=='0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------------------------------------------
# PART 2 - Data Cleaning
# ------------------------------------------------------
def Replace_Missing_Numeric_With_0():
    df = pd.read_csv("Data.csv")
    df = df.fillna(0)
    df.to_csv("cleaned_data_without_missing_numeric.csv", index=False)
    print("Dataset cleaned and saved as cleaned_data_without_missing_numeric.csv")

def Remove_Duplicates():
    df = pd.read_csv("Data.csv")
    df.drop_duplicates(inplace=True)
    df.to_csv("cleaned_data_without_duplicates.csv", index=False)
    print("Duplicates removed and saved as cleaned_data_without_duplicates.csv")

def Data_Cleaning():
    while True:
        print("   === Data Cleaning ===   ")
        print("1. Remove Missing Numeric with 0.")
        print("2. Remove duplicates.")
        print("0. Exit.")
        choice = input("Enter your choice: ")
        if choice=='1':
            Replace_Missing_Numeric_With_0()
        elif choice =='2' : 
            Remove_Duplicates()
        elif choice=='0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------------------------------------------
# PART 3 -Subsetting & Filtering
# ------------------------------------------------------

def high_earners():
    df = pd.read_csv("Data.csv")
    df["BasePay"] = pd.to_numeric(df["BasePay"], errors='coerce')
    high = df[df["BasePay"] > 100000]
    print(high)

def employees_2013():
    df = pd.read_csv("Data.csv")
    df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
    emp_2013 = df[df["Year"] == 2013]
    print(emp_2013)

def police_jobs():
    df = pd.read_csv("Data.csv")
    df["JobTitle"] = df["JobTitle"].fillna("")
    police = df[df["JobTitle"].str.contains("POLICE",case=False, na=False)]
    print(police)

def Subsetting_And_Filtering():
    while True:
        print("   === Subsetting And Filtering ===   ")
        print("1. Create a subset of High Earners (Base Pay > 100000).")
        print("2. Create a subset of Employees from year 2013.")
        print("3. Create a subset of JobTitles containing “POLICE”.")
        print("0. Exit.")
        choice = input("Enter your choice: ")
        if choice=='1':
            high_earners()
        elif choice =='2' : 
            employees_2013()
        elif choice=='3':
            police_jobs()
        elif choice=='0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------------------------------------------
# PART 4 - New Columns & Summary Statistics
# ------------------------------------------------------

def create_is_manager_column():
    df = pd.read_csv("Data.csv")
    df["Is_Manager"] = df["JobTitle"].str.contains("MANAGER|CHIEF",case=False,na=False)
    df.to_csv("manager_data.csv", index=False)
    print("Column 'Is_Manager' created successfully and saved as manager_data.csv.")

def Create_Computed_Columns():
    while True:
        print("   === Create Computed Columns ===   ")
        print("1.Create a computed column Is_Manager if the job title contains 'MANAGER' or 'CHIEF'.")
        print("0. Exit.")
        choice = input("Enter your choice: ")
        if choice=='1':
            create_is_manager_column()
        elif choice=='0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
    
def Summary_Statistics():
    data = pd.read_csv('Data.csv')
    data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

    average_basepay = data['BasePay'].mean()
    top_5_titles = data['JobTitle'].value_counts().head(5)
    total_employees = data['EmployeeName'].nunique()

    print("SUMMARY STATISTICS")
    print("------------------")
    print("Total number of employees:", total_employees)
    print("Average BasePay:", average_basepay)
    print("\nTop 5 most common job titles:")
    print(top_5_titles)

# ------------------------------------------------------
# PART 5 - Grouping & Aggregation
# ------------------------------------------------------

def average_pay_year():
    data = pd.read_csv("Data.csv")
    average_totalpay_per_year = data.groupby('Year')['TotalPay'].mean()
    print(average_totalpay_per_year)

def Grouping_And_Aggregation():
    while True:
        print("   === Analysis using group based aggregation ===   ")
        print("1. Average TotalPay per Year.")
        print("0. Exit.")
        choice = input("Enter your choice: ")
        if choice=='1':
            average_pay_year()
        elif choice=='0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------------------------------------------
#                PART 6 - Joining
# ------------------------------------------------------

def joining():
    df = pd.read_csv("Data.csv",low_memory=False)
    agency_df =pd.read_csv("agency_codes.csv")
    merged_df = pd.merge(df, agency_df, on="Agency", how="left")
    merged_df.to_csv("merged_data.csv", index=False)
    print("Joining completed, Please check 'merged_data.csv'. ")


# ------------------------------------------------------
#         PART 7 - Interactive Investigation Script
# ------------------------------------------------------


def filter_by_JobTitle(keyword):
    df = pd.read_csv("Data.csv",low_memory=False)
    filtered_df=df[df['JobTitle'].str.contains(keyword, case=False,na=False)]
    if filtered_df.empty:
        print("No Job Title corresponds to your entry.")
    else :
        print(filtered_df)

def number_of_matches_by_JobTitle(keyword):
    df_cleaned = pd.read_csv("cleaned_data_without_missing_numeric.csv")
    filtered_df=df_cleaned[df_cleaned['JobTitle'].str.contains(keyword, case=False,na=False)]
    return len(filtered_df)

def average_BasePay(keyword):
    df_cleaned = pd.read_csv("cleaned_data_without_missing_numeric.csv")
    df_cleaned['BasePay'] = pd.to_numeric(df_cleaned['BasePay'],errors='coerce')
    filtered_df=df_cleaned[df_cleaned['JobTitle'].str.contains(keyword, case=False,na=False)]
    avg_basepay =filtered_df['BasePay'].mean()
    return avg_basepay


def highest_total_pay(keyword):
    df_cleaned = pd.read_csv("cleaned_data_without_missing_numeric.csv")
    df_cleaned['TotalPay'] = pd.to_numeric(df_cleaned['TotalPay'],errors='coerce')
    filtered_df=df_cleaned[df_cleaned['JobTitle'].str.contains(keyword, case=False,na=False)]
    Max_totalPay=filtered_df['TotalPay'].max()
    return Max_totalPay


def save_changes(keyword): 
    with open("custom_search.csv",'a') as f :
        df = pd.read_csv("Data.csv")
        f.write(f"The job title keyword is {keyword}\n")
        f.write(f"The number of matches by job title : {number_of_matches_by_JobTitle(keyword)}\n")
        f.write(f"The average base pay : {average_BasePay(keyword)}\n")
        f.write(f"The highest total pay : {highest_total_pay(keyword)}\n")
    print("This filter has been saved succesfully in 'custom_search.csv' .  ")

def Interactive_Investigation():
    test1=True
    keyword=input("enter keyword for job title :")
    while test1 :
        print("   ===Interactive Investigation Script===   ")
        print("1. Filter job title using keywords.")
        print("2. Show the number of matches.")
        print("3. Show the average base pay.")
        print("4. Show the highest total pay.")
        print("5. Save.")
        print("6. Change keyword")
        print("0. Exit.")
        test=False
        while test==False:
            choice=str(input("Enter your choice : "))
            test = (choice=='1'or choice=='2' or choice=='3' or choice=='4' or choice=='5' or choice =='6' or choice=='0')
        
        if choice=='1':
            filter_by_JobTitle(keyword)
        elif choice =='2' : 
            print("Number of matches:", number_of_matches_by_JobTitle(keyword))
        elif choice=='3': 
            print("Average BasePay:", average_BasePay(keyword))
        elif choice=='4':
            print("Highest TotalPay:", highest_total_pay(keyword))
        elif choice=='5':
            save_changes(keyword)
        elif choice == '6':
            keyword = input("Enter new keyword: ")
            print("Keyword updated.")
        elif choice=='0':
            return 0
        else : 
            print("Invalid choice. Try again.")
        test1= choice!='0'
