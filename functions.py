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
