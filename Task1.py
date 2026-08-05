# Temperature Converter (Celsius <-> Fahrenheit)

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Menu Display
print("--- Temperature Unit Converter ---")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = input("Select an option (1 or 2): ")

if choice == "1":
    c_temp = float(input("Enter temperature in °C: "))
    f_result = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C is equal to {f_result:.2f}°F")

elif choice == "2":
    f_temp = float(input("Enter temperature in °F: "))
    c_result = fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is equal to {c_result:.2f}°C")

else:
    print("Invalid selection. Please run the program again and choose 1 or 2.")