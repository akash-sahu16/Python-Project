def calculator():
    print("Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Cube")
    print("8. Cube Root")
    print("9. BMI (Body Mass Index)")
    print("10. Percentage")
    print("11. Speed")
    print("12. Time")
    print("13. Density")
    print("14. Temperature Conversion")
    print("15. Binary Digits Conversion")

    # Get user's choice of operation
    choice = input("Enter choice (1-15): ")

    if choice in ('1', '2', '3', '4'):
        # For addition, subtraction, multiplication, and division
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            # Addition
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            # Subtraction
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            # Multiplication
            result = num1 * num2
            print("Result:", result)
        else:
            if num2 != 0:
                # Division
                result = num1 / num2
                print("Result:", result)
            else:
                print("Error: Division by zero is not allowed.")
    elif choice == '5':
        # Square
        num = float(input("Enter the number: "))
        result = num ** 2
        print("Result:", result)
    elif choice == '6':
        # Square Root
        num = float(input("Enter the number: "))
        if num >= 0:
            result = num ** 0.5
            print("Result:", result)
        else:
            print("Error: Cannot calculate square root of a negative number.")
    elif choice == '7':
        # Cube
        num = float(input("Enter the number: "))
        result = num ** 3
        print("Result:", result)
    elif choice == '8':
        # Cube Root
        num = float(input("Enter the number: "))
        result = num ** (1 / 3)
        print("Result:", result)
    elif choice == '9':
        # BMI (Body Mass Index)
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))
        bmi = weight / (height ** 2)
        print("BMI:", bmi)
    elif choice == '10':
        # Percentage
        num = float(input("Enter the number: "))
        percentage = float(input("Enter the percentage: "))
        result = (num * percentage) / 100
        print("Result:", result)
    elif choice == '11':
        # Speed
        distance = float(input("Enter distance in meters: "))
        time = float(input("Enter time in seconds: "))
        speed = distance / time
        print("Speed:", speed)
    elif choice == '12':
        # Time
        distance = float(input("Enter distance: "))
        speed = float(input("Enter speed: "))
        time = distance / speed
        print("Time:", time)
    elif choice == '13':
        # Density
        mass = float(input("Enter mass in kilograms: "))
        volume = float(input("Enter volume in cubic meters: "))
        density = mass / volume
        print("Density:", density)
    elif choice == '14':
        # Temperature Conversion
        temperature = float(input("Enter temperature: "))
        unit_from = input("Enter unit to convert from (C/F/K): ")
        unit_to = input("Enter unit to convert to (C/F/K): ")
        converted_temperature = convert_temperature(temperature, unit_from, unit_to)
        print(f"{temperature} {unit_from} is equivalent to {converted_temperature} {unit_to}")
    elif choice == '15':
        # Binary Digits Conversion
        number = int(input("Enter a decimal number: "))
        print("Binary:", bin(number))
        print("Octal:", oct(number))
        print("Hexadecimal:", hex(number))
    else:
        print("Invalid input. Please try again.")

def convert_temperature(temperature, unit_from, unit_to):
    if unit_from == 'C':
        if unit_to == 'F':
            return (temperature * 9/5) + 32
        elif unit_to == 'K':
            return temperature + 273.15
    elif unit_from == 'F':
        if unit_to == 'C':
            return (temperature - 32) * 5/9
        elif unit_to == 'K':
            return (temperature + 459.67) * 5/9
    elif unit_from == 'K':
        if unit_to == 'C':
            return temperature - 273.15
        elif unit_to == 'F':
            return (temperature * 9/5) - 459.67

# Example usage
calculator()
