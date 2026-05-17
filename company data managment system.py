import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main_menu():
    print("Companies Data")
    print("\n")

    print("Data Analysis")
    print("1. Reading complete csv report")
    print("2. Display Record of top MNC's without index")
    print("\n")

    print("Data Visualization")
    print("3. Line chart")
    print("4. Bar chart")
    print("\n")

    print("Data Manipulation")
    print("5. Specific number of companies from the top")
    print("6. Specific number of companies from bottom")
    print("7. Sorting the data as per your choice")
    print("8. Updating Adding new data")
    print("9. Deleting the column")
    print("10. Specific column")


main_menu()


def ReadCSV():
    print("Reading complete csv report")

    df = pd.read_csv(r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv")
    print(df)



def no_index():
    print("Display Record of top MNC's")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv",
        index_col=0
    )

    print(df)



def Line_chart():
    x = [
        22.1, 1000, 58604, 1468000,
        150028, 110000, 935000,
        342982, 276319, 12000, 11300
    ]

    y = [
        2135, 36, 1053.5,
        1420, 710.78,
        260, 229,
        79.06, 2,
        131.6
    ]

    plt.plot(x, y)

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Line Chart")

    plt.show()



def Bar_chart():

    x = [
        22.1, 1000, 58604,
        1468000, 150028,
        110000, 935000,
        342982
    ]

    y = [
        2135, 36, 1053.5,
        1420, 710.78,
        260, 229,
        79.06
    ]

    plt.bar(x, y)

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Bar Chart")

    plt.show()



def companies_from_top():
    print("Companies from top")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    n = int(input("Enter number of rows: "))

    print(df.head(n))



def companies_from_bottom():
    print("Companies from bottom")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    n = int(input("Enter number of rows: "))

    print(df.tail(n))



def data_sorting():
    print("Data sorting")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    df.sort_values(by=["Company Name"], inplace=True)
    print(df, "\n")



def Updating_Adding_new_data():
    print("Updating Adding new data")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    print(df)

    h = input("Enter column heading: ")
    det = eval(input("Enter data: "))

    df[h] = pd.Series(data=det, index=df.index)

    print(df)



def Deleting_the_column():
    print("Deleting the column")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    a = input("Enter column name to delete: ")

    df.drop([a], axis=1, inplace=True)

    print(df)



def specific_company():
    print("Search for details of a specific company")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    col = input("Enter company name whose detail you want to see: ")

    print(df[col])



def Column_Renaming():

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    print(df)

    n = input("Enter old column name: ")
    N = input("Enter new column name: ")

    df.rename(columns={n: N}, inplace=True)

    print("\nAfter modifying column:\n")
    print(df)

    print("Column renamed")



def Deleting_the_row():
    print("Deleting the row")

    df = pd.read_csv(
        r"C:\Users\Panshul Sharma\Documents\CSV\Companies Data.csv"
    )

    a = input("Enter Company Name which need to be deleted: ")

    df.drop(df.index[df["Company Name"] == a], inplace=True)

    print(df)

    print("Row deleted")


option = 'y'

while option == 'y':

    opt = int(input("Enter your choice: "))

    if opt == 1:
        ReadCSV()

    elif opt == 2:
        no_index()

    elif opt == 3:
        Line_chart()

    elif opt == 4:
        Bar_chart()

    elif opt == 5:
        companies_from_top()

    elif opt == 6:
        companies_from_bottom()

    elif opt == 7:
        data_sorting()

    elif opt == 8:
        Updating_Adding_new_data()

    elif opt == 9:
        Deleting_the_column()

    elif opt == 10:
        specific_company()

    else:
        print("INVALID NUMBER!!!")

    option = input("Type y to continue or n to exit: ")

