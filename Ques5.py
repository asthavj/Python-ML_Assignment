#5 Write a program that takes a string input from the user and writes it to a text file.
def write_to_file(input_string, file_name):
    try:
        with open(file_name, 'w') as text_file:
            text_file.write(input_string)
        print("String written to file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_string = input("Enter a string to write to the file: ")

file_name = "output.txt"


write_to_file(input_string, file_name)
