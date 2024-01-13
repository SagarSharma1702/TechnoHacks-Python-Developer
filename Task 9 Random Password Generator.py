"""
Task 9 : Random Password Generator
Create a program that generates a random 
password of a user-defined length.
"""
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive number.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

# Call the password_generator function to generate a random password
password_generator()
