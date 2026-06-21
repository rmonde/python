def convert_temperature(value):
    return (value * 9/5) + 32;


if __name__ == "__main__":
    try:
        temp_value = float(input("Enter the temperature value: "))
        converted_value = convert_temperature(temp_value)
        print(f"The converted temperature is: {converted_value}")
    except ValueError as e:
        print(f"Invalid input. Please enter a valid temperature value: {e}")