# Modular Temperature Converter Script

A lightweight, beginner-friendly Python script built for converting temperature values between **Celsius** and **Fahrenheit**. This project demonstrates modular functional programming, user input validation, and dynamic console output formatting.

---

## 📌 Features

* **Bi-Directional Conversion:** Convert from Celsius to Fahrenheit and vice-versa.
* **Modular Code Structure:** Uses dedicated Python functions (`def`) for clear separation of concerns.
* **Interactive CLI Menu:** User-friendly menu driven by basic control flow (`if-elif-else`).
* **Formatted Output:** Formats numerical float outputs to two decimal places for clear output metrics.

---

## 🧮 Conversion Formulas

* **Celsius to Fahrenheit:** 
  $$F = \left(C \times \frac{9}{5}\right) + 32$$

* **Fahrenheit to Celsius:** 
  $$C = (F - 32) \times \frac{5}{9}$$

---

## 💻 Script Implementation

```python
# Temperature Converter (Celsius <-> Fahrenheit)

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
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
```

🚀 How to Run
Open your terminal or VS Code.

Navigate to your project folder:
Bash
```cd Task-01-Python-Basics```

Run the Python script:
Bash
```python task01_temp_converter.py```


