import pandas as pd
# PART 1 - File Handling

def preview_dataset():
    with open("Data.csv", "r") as f:
        for i in range(5):
            print(f.readline())

def search_chief():
    with open("Data.csv", "r") as f:
        for line in f:
            if "chief" in line.lower():
                print(line.strip())

def extract_two_columns():
    column1 = int(input("Enter the index of the first column (starting from 0): "))
    column2 = int(input("Enter the index of the second column (starting from 0): "))

    with open("Data.csv", "r") as f:
        for line in f:
            columns = line.strip().split(",")

            if len(columns) > column1 and len(columns) > column2:
                print(columns[column1], "|", columns[column2])

# PART 2 - Data Cleaning
def clean_dataset():
    df = pd.read_csv("Data.csv")
    df = df.fillna(0)
    df['BasePay'] = df['BasePay'].replace(['not provided', 'Not Provided', 'NOT PROVIDED'], 0)
    df.drop_duplicates(inplace=True)
    df.to_csv("cleaned_data.csv")
    print("Dataset cleaned and saved as cleaned_data.csv")

# PART 3 -Subsetting & Filtering
def high_earners():
    df = pd.read_csv("Data.csv")
    high = df[df["BasePay"] > 100000]
    print(high)

def employees_2013():
    df = pd.read_csv("Data.csv")
    emp_2013 = df[df["Year"] == 2013]
    print(emp_2013)

def police_jobs():
    df = pd.read_csv("Data.csv")
    police = df[df["JobTitle"].str.contains("POLICE")]
    print(police)

# PART 4 - New Columns & Summary Statistics

def create_is_manager_column():
    df = pd.read_csv("Data.csv")
    df["Is_Manager"] = df["JobTitle"].str.contains("MANAGER|CHIEF")
    df.to_csv("manager_data.csv", index=False)
    print("Column 'Is_Manager' created successfully and saved as manager_data.csv.")

def summary_statistics():
    df = pd.read_csv("Data.csv")
    total_employees = len(df)
    average_basepay = df["BasePay"].mean()
    top_titles = df["JobTitle"].value_counts().head(5)

    print("SUMMARY STATISTICS")
    print("------------------")
    print("Total number of employees:", total_employees)
    print("Average BasePay:", average_basepay)
    print("\nTop 5 most common job titles:")
    print(top_titles)

# ------------------------------------------------------
#      PART VII - Interactive Investigation Script
# ------------------------------------------------------
import pandas as pd 
df = pd.read_csv("data - data.csv")

def filter_by_JobTitle():
    while True:
        keyword=input("enter the job title to search for : ")
        if keyword.lower()!="not provided" :
            break
    filtered_df=df[df['JobTitle'].str.contains(keyword, case=False,na=False)]
    if filtered_df.empty:
        print("No Job Title corresponds to your entry.")
    else :
        print(filtered_df)

def number_of_matches_by_JobTitle(keyword):
    filtered_df=df[df['JobTitle'].str.contains(keyword, case=False,na=False)]
    return len(filtered_df)

def average_BasePay(keyword):
    df_cleaned = pd.read_csv("cleaned_data.csv")
    filtered_df=df_cleaned[df_cleaned['JobTitle'].str.contains(keyword, case=False,na=False)]

    avg_basepay =filtered_df['BasePay'].mean()
    return avg_basepay


def highest_total_pay(keyword):
    df_cleaned = pd.read_csv("cleaned_data.csv")
    filtered_df=df_cleaned[df_cleaned['JobTitle'].str.contains(keyword, case=False,na=False)]
    Max_totalPay=filtered_df['TotalPay'].max()
    return Max_totalPay


def save_changes(keyword): 
    with open("custom_search.csv",'a') as f :
        df = pd.read_csv("data - data.csv")
        f.write(f"The number of matches by job title : {number_of_matches_by_JobTitle(keyword)}\n")
        f.write(f"The average base pay : {average_BasePay(keyword)}\n")
        f.write(f"The highest total pay : {highest_total_pay(keyword)}\n")

def Interactive_Investigation():
    print("   ===Interactive Investigation Script===   ")
    print("1. Filter job title using keywords.")
    print("2. Show the number of matches.")
    print("3. Show the average base pay.")
    print("4. Show the highest total pay.")
    print("5. Save.")
    print("6. Exit.")
    keyword=input("enter keyword for job title :")
    test=False
    while test==False:
        choice=str(input("Enter your choice : "))
        test = (choice=='1'or choice=='2' or choice=='3' or choice=='4' or choice=='5' or choice=='0')
    if choice=='1':
        filter_by_JobTitle(keyword)
    elif choice =='2' : 
        print(number_of_matches_by_JobTitle(keyword))
    elif choice=='3': 
        print(average_BasePay(keyword))
    elif choice=='4':
        print(highest_total_pay(keyword))
    elif choice=='5':
        save_changes()
    elif choice=='0':
        return 0
    
