# shopping_list_manager.py

def display_menu():
        # Display the menu
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
def main():
    shopping_list = []  # Start with an empty list
    
    while True:
        
        # Get user choice
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f'"{item}" has been added to the shopping list.')
        
        elif choice == '2':
            # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from the shopping list.')
            else:
                print(f'"{item}" is not in the shopping list.')
        
        elif choice == '3':
            # View list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nShopping list is empty.")
        
        elif choice == '4':
            # Exit
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the shopping list manager
if __name__ == "__main__":
    shopping_list_manager()

