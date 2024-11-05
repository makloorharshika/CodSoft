import random
import string

# Function to generate a password
def generate_password(length):
    # Define character sets for password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to run the password generator
def main():
    print("Password Generator")
    
    # Get the desired length of the password from the user
    try:
        length = int(input("Enter the desired length for the password: "))
        
        if length < 6:
            print("Warning: For better security, a password length of at least 6 characters is recommended.")
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")

# Run the main function
if __name__ == "__main__":
    main()
