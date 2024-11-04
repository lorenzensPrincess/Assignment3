import csv  

class InventoryItem:
    # The class representing an inventory item with essential characteristics. 
    
    # Initialize each inventory item with specific attributes
    def __init__(self, name, quantity, location, last_maintenance, serial_number, category):
        self.name = name  # Name of the item
        self.quantity = quantity  # Quantity of the item in stock
        self.location = location  # Location of the item 
        self.last_maintenance = last_maintenance  # Date of the last maintenance check for the item
        self.serial_number = serial_number  # The serial number for the item.
        self.category = category  # Category the item belongs to (ex:tools,electronics).

class InventoryManager:
    def __init__(self):
        # Creating an empty list to store all inventory items.
        self.inventory = []

    # A method to add a new item to the inventory.
    def add_item(self):
        try:
            # Gathering input from the user for each characteristic of the new item.
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity (numbers only): "))  # Ensuring that the quantity is an integer.
            location = input("Enter location: ")
            last_maintenance = input("Enter last maintenance date (YYYY-MM-DD): ")
            serial_number = input("Enter serial number: ")  # The serial number must be added to avoid duplicates.
            category = input("Enter category: ")
            
            # Creation of a new InventoryItem object that has been provided by the user. 
            new_item = InventoryItem(name, quantity, location, last_maintenance, serial_number, category)
            
            # Adding the new item to the inventory list.
            self.inventory.append(new_item)
            print(f"Item '{name}' added successfully!\n")
        
        # Error handling - when the input given by the user is invalid. 
        except ValueError:
            print("Error: Quantity must be a number. Please try again with a valid input.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

    # A method to update an existing item in the inventory, based on its serial number that the user provided earlier. 
    def update_item(self):
        serial_number = input("Enter serial number of the item to update: ")
        found = False  

        # This loops through the inventory list to find the item by its serial number.
        for item in self.inventory:
            if item.serial_number == serial_number:
                found = True  # It is marked as found if the serial number matches.
                print(f"Updating item: {item.name}")
                
                try:
                    # A prompt for new values, allowing the user to update each attribute
                    item.quantity = int(input("Enter new quantity (numbers only): "))
                    item.location = input("Enter new location: ")
                    item.last_maintenance = input("Enter new last maintenance date (YYYY-MM-DD): ")
                    print("Item updated successfully!\n")
                
                # Eroor handling - when the quantity input is not a number.
                except ValueError:
                    print("Error: Quantity must be a number. Please enter a valid number.\n")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}\n")
                break  # Exits the loop once the item is found and updated. 
        
        # If no item is found with the given serial number, an error message is sent to the user. 
        if not found:
            print(f"No item found with serial number {serial_number}. Please double-check the serial number.\n")

    # A method to remove an item from the inventory based on its serial number.
    def remove_item(self):
        serial_number = input("Enter serial number of the item to remove: ")
        found = False  

        # This loops through the inventory to find and remove the item with the same serial number.
        for item in self.inventory:
            if item.serial_number == serial_number:
                self.inventory.remove(item)  # Remove the item of the given serial number from the list. 
                print(f"Item '{item.name}' removed successfully!\n")
                found = True
                break  # Exits the loop once item is found and removed. 

        # If no item is found, then the user receives an error message the user.
        if not found:
            print(f"No item found with serial number {serial_number}. Check the serial number and try again.\n")

    # A method to generate a report of all inventory items and save it. 
    def generate_report(self):
        try:
            # This is to open a new CSV file in write mode.
            with open('inventory_report.csv', mode='w', newline='') as file:
                writer = csv.writer(file)  
                
                # The characteristics of the item should be given by the user. 
                writer.writerow(["Name", "Quantity", "Location", "Last Maintenance Date", "Serial Number", "Category"])
                
                # Writing each item's characteristics as a row.
                for item in self.inventory:
                    writer.writerow([item.name, item.quantity, item.location, item.last_maintenance, item.serial_number, item.category])
            
            # Confirms the user that the report was generated successfully. 
            print("Inventory report generated successfully as 'inventory_report.csv'.\n")
        
        # Error handling - when any unexpected errors occur while handling the file. 
        except Exception as e:
            print(f"Error generating report: {e}\n")


# Providing the user a menu-driven interface by defining the main function.
def main():
    """Main function to handle user interactions."""
    manager = InventoryManager()  
    
    # A loop to display menu options and process choices of the user. 
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Generate Report")
        print("5. Exit")
        
        # Getting the user's choice.
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            manager.add_item()  # Run add_item if user selects 1
        elif choice == '2':
            manager.update_item()  # Run update_item if user selects 2
        elif choice == '3':
            manager.remove_item()  # Run remove_item if user selects 3
        elif choice == '4':
            manager.generate_report()  # Run generate_report if user selects 4
        elif choice == '5':
            print("Exiting the program.")
            break  # Exit the loop and sends a feedback to the user. 
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")  # Feedback will be sent to the user regarding the invalid input from the user. 


# Jumps back to the main program and runs it. l
main()
