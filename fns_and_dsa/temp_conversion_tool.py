# Define Global Conversion Factors
#FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    try:
        # Prompt user for input
        temperature = float(input("Enter the temperature: "))
        scale = input("Specify the scale (C for Celsius, F for Fahrenheit): ").strip().upper()
        
        # Perform conversion based on the scale
        if scale == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F.")
        elif scale == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C.")
        else:
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()

