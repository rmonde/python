import math

def calculate_circumference(radius):
    return 2 * 3.14159 * radius

def calculate_area(radius):
    return math.pi * radius * 2

if __name__ == "__main__":
    try:
        radius_input = float(input("Enter the radius of the circle: "))
        circumference = calculate_circumference(radius_input)
        area = calculate_area(radius_input)
        print(f"The circumference of the circle is: {circumference}")
        print(f"The area of the circle (using Math) is: {area}")
    except ValueError as e:
        print(f"Invalid input, please enter a valid number: {e}")