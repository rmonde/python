def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def string_lower(s):
    return s.lower()

def string_upper(s):
    return s.upper()

def slice_string(s):
    return s[1:]

if __name__ == "__main__":
    try:
        input_string = str(input("Enter a string to reverse: "))
        reversed_string = reverse_string(input_string)
        print(f"Reversed string: {reversed_string}")
        capitalized_string = capitalize_string(input_string)
        print(f"Capitalized string: {capitalized_string}")
        lower_string = string_lower(input_string)
        print(f"Lowercase string: {lower_string}")
        upper_string = string_upper(input_string)
        print(f"Uppercase string: {upper_string}")
        sliced_string = slice_string(input_string)
        print(f"Sliced string (without first character): {sliced_string}")
    except ValueError as e:
        print(f"Invalid input, please enter a valid string: {e}")