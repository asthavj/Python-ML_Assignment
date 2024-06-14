#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)

    if starts_with_prefix and ends_with_suffix:
        return f"The string '{input_string}' starts with '{prefix}' and ends with '{suffix}'."
    elif starts_with_prefix:
        return f"The string '{input_string}' starts with '{prefix}' but does not end with '{suffix}'."
    elif ends_with_suffix:
        return f"The string '{input_string}' ends with '{suffix}' but does not start with '{prefix}'."
    else:
        return f"The string '{input_string}' does not start with '{prefix}' and does not end with '{suffix}'."


input_string = "Hello World!"
prefix = "Hello"
suffix = "!"

result = check_prefix_suffix(input_string, prefix, suffix)
print(result)
