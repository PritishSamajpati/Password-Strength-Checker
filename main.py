import re

def password_strength(password):
    """
    Function to check the strength of a password.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your password is secure!"

def main():
    """
    Main function to take user input and check password strength.
    """
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        
        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker! Goodbye!")
            break

        # Run the password strength checker tool
        strength = password_strength(password)
        print(strength)

if __name__ == "__main__":
    main()