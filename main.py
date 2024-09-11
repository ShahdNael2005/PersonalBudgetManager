import json

# Function to add income
def add_income(budget_data):
    description = input("Enter income description: ")
    amount = float(input("Enter amount: "))
    budget_data['income'].append((description, amount))
    print("Income added successfully!")

# Function to add expense
def add_expense(budget_data):
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    budget_data['expenses'].append((description, amount))
    print("Expense added successfully!")

# Function to calculate and display balance
def calculate_balance(budget_data):
    total_income = sum([amount for desc, amount in budget_data['income']])
    total_expense = sum([amount for desc, amount in budget_data['expenses']])
    balance = total_income - total_expense
    print(f"\nTotal Income: ${total_income}")
    print(f"Total Expenses: ${total_expense}")
    print(f"Current Balance: ${balance}")

# Function to save data to a file
def save_data(budget_data, file_name='budget_data.txt'):
    with open(file_name, 'w') as file:
        json.dump(budget_data, file)
    print("Data saved to file successfully!")

# Function to load data from a file
def load_data(file_name='budget_data.txt'):
    try:
        with open(file_name, 'r') as file:
            content = file.read().strip()  # Read and strip any extra spaces/newlines
            if not content:  # If the file is empty, initialize it
                return {'income': [], 'expenses': []}
            return json.loads(content)  # Parse JSON content if the file has data
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or has invalid JSON, return a new budget structure
        return {'income': [], 'expenses': []}


# Main menu to navigate the budget manager
def main():
    budget_data = load_data()  # Load data from file on startup

    while True:
        print("\nPersonal Budget Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_income(budget_data)
        elif choice == '2':
            add_expense(budget_data)
        elif choice == '3':
            calculate_balance(budget_data)
        elif choice == '4':
            save_data(budget_data)  # Save data before exiting
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point for the application
if __name__ == "__main__":
    main()
