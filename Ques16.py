def count_character_frequencies(input_string):
    frequency_dict = {}
    for char in input_string:    # Loop through each character in the input string
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict


input_string = "Welcome to coding world"
frequencies = count_character_frequencies(input_string)
print(frequencies)
