#27. Write a program in python that converts a string into a list of its characters
def string_to_list(input_string):
  
    return [char for char in input_string]


input_string = "Hello, World!"
character_list = string_to_list(input_string)

print("The list of characters is:", character_list)

