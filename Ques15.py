#15 Write a program that reads data from a CSV file and prints it to the console.
import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)
        print("CSV file read successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = "industry.csv"
read_csv_file(file_name)
