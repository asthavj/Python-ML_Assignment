#19 Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):

    cleaned_string = ''.join([char for char in input_string if char not in string.punctuation])
    return cleaned_string

input_string = input("Enter a string: ")
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)

