def sort_numbers(numbers):
    """Sort a list of numbers in ascending order."""
    return sorted(numbers)

if __name__ == "__main__":
    # Accept input from the user
    try:
        input_numbers = input("Enter a list of numbers separated by commas: ")
        # Convert the input string into a list of integers
        numbers_list = [int(num.strip()) for num in input_numbers.split(",")]
        # Sort the numbers and print the result
        sorted_numbers = sort_numbers(numbers_list)
        print("Sorted numbers:", sorted_numbers)
    except ValueError as e:
        print(f"Invalid input. Please enter a list of numbers separated by commas. {e}")