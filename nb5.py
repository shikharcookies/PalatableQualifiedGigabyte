stack = []  # Initialize an empty list to act as the stack

def push():
    """Function to add an element to the top of the stack"""
    element = input("Enter the element to push onto the stack: ")
    stack.append(element)
    print(f"{element} pushed onto the stack.")

def pop():
    """Function to remove the top element from the stack"""
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        element = stack.pop()
        print(f"{element} popped from the stack.")

def display():
    """Function to display the contents of the stack"""
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack contents: ")
        for element in reversed(stack):
            print(element)

while True:
    # Display the menu
    print("\nSTACK OPERATIONS MENU")
    print("1. Push element onto stack")
    print("2. Pop element from stack")
    print("3. Display stack contents")
    print("4. Exit program")

    # Get user input for the menu choice
    choice = input("Enter your choice: ")

    # Perform the selected operation
    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        display()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice from the menu.")