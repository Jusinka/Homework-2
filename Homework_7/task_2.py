def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def temperature_converter(value, input_scale):
    if input_scale == "C":
        celsius = value
    elif input_scale == "F":
        celsius = fahrenheit_to_celsius(value)
    elif input_scale == "K":
        celsius = kelvin_to_celsius(value)
    else:
        print("Неправильний тип температури. Використовуйте C, F або K.")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)

    return celsius, fahrenheit, kelvin

def main():
    value = float(input("Введіть значення температури: "))
    input_scale = input("Введіть тип температури (C, F, K): ").upper()

    celsius, fahrenheit, kelvin = temperature_converter(value, input_scale)

    print(f"{value} {input_scale} = {celsius:.2f} C, {fahrenheit:.2f} F, {kelvin:.2f} K")

if __name__ == "__main__":
    main()