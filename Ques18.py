#18 Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(string1, string2):

    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    if len(string1) != len(string2):
        return False

    # Create dictionaries to count the frequency of each character in both strings
    char_count1 = {}
    char_count2 = {}

    for char in string1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in string2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    return char_count1 == char_count2


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")