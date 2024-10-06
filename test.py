# Simple Python program to greet the user

def greet_user():
    # Ask for user's name
    name = input("What is your name? ")
    
    # Ask for user's age
    age = input("How old are you? ")
    
    # Create a greeting message
    greeting = f"Hello, {name}! You are {age} years old."
    
    # Print the greeting message
    print(greeting)

# Call the function to run the program
greet_user()
