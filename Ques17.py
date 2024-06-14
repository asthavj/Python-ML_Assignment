#17 Write a program in python that converts a given string to title case (first letter of each word capitalized).

def to_title_case(input_string):
    title_cased_string = input_string.title()# Use the title() method to convert the string to title case
    return title_cased_string

input_string = "hello world! welcome to python programming."
title_cased_string = to_title_case(input_string)
print(title_cased_string)
