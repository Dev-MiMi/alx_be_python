
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR *= (number - 32)
    return FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = (CELSIUS_TO_FAHRENHEIT_FACTOR * number) + 32
    return CELSIUS_TO_FAHRENHEIT_FACTOR

number = float(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if temp == "F":
    result = convert_to_celsius(FAHRENHEIT_TO_CELSIUS_FACTOR)
    print(f"{number}°F is {result}°C")
elif temp == "C":
    result = convert_to_fahrenheit(CELSIUS_TO_FAHRENHEIT_FACTOR)
    print(f"{number}°C is {result}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
