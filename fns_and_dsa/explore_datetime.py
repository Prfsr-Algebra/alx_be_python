# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    """
    Calculate a future date based on a user-specified number of days.
    """
    # Prompt the user for the number of days to add
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)  # Calculate future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    calculate_future_date(current_date)

