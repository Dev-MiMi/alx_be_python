
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

number = float(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp == "F":
    result = convert_to_celsius(number)
    print(f"{number}°F is {result}°C")
elif temp == "C":
    result = convert_to_fahrenheit(number)
    print(f"{number}°C is {result}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
