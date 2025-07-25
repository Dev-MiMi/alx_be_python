number = float(input("Enter the temperature to convert: "))

temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 * (number - 32)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5 * number) + 32
if temp == "F":
    def convert_to_celsius(fahrenheit):
        return FAHRENHEIT_TO_CELSIUS_FACTOR
    result = convert_to_celsius(FAHRENHEIT_TO_CELSIUS_FACTOR)
    print(f"{number}°F is {result}°C")
elif temp == "C":
    def convert_to_fahrenheit(celsius):
        return CELSIUS_TO_FAHRENHEIT_FACTOR
    result = convert_to_fahrenheit(CELSIUS_TO_FAHRENHEIT_FACTOR)
    print(f"{number}°C is {result}°F")
