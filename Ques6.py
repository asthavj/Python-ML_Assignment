# Write a program that reads the content of a text file and prints it to the console.
def read_file(file_name):
    try:
        with open(file_name, 'r') as text_file:
            content = text_file.read()
        print("Content of the file:")
        print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = "example.txt"


read_file(file_name)
