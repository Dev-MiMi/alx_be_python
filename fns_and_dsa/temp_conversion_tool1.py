FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

number = float(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp == "F":
    result = convert_to_celsius(number)  # Fixed: Pass number, not factor
    print(f"{number}°F is {result:.2f}°C")
elif temp == "C":
    result = convert_to_fahrenheit(number)  # Fixed: Pass number, not factor
    print(f"{number}°C is {result:.2f}°F")
else:
    print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
