# -------------------------
# PART I - File Handling
# -------------------------

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