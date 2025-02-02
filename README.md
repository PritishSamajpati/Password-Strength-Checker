# Password-Strength-Checker

## Project Overview

The Password Strength Checker is a Python-based tool designed to evaluate the robustness of user passwords. It assesses passwords based on various criteria, providing feedback to help users enhance their password security.

## Use Cases

- **Personal Security**: Individuals can use this tool to test the strength of their passwords and receive suggestions for improvement.
- **Educational Purposes**: Educators can demonstrate the importance of strong passwords and the factors that contribute to password strength.
- **Development Reference**: Developers can reference this implementation when building password validation features into their applications.

## Code Explanation

The core functionality is implemented in Python, utilizing regular expressions and string methods to evaluate password strength.

```python
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
```

**Functionality**:

- **Length Check**: Ensures the password is at least 8 characters long.
- **Numeric Character Check**: Verifies the inclusion of at least one digit.
- **Uppercase and Lowercase Checks**: Confirms the presence of both uppercase and lowercase letters.
- **Special Character Check**: Encourages the use of special characters for enhanced security.

The `main` function facilitates user interaction, allowing continuous password evaluations until the user decides to exit.

## Conclusion

This Password Strength Checker serves as a practical tool for assessing and improving password security. By following the feedback provided, users can create stronger passwords, thereby enhancing their protection against unauthorized access.

For a visual demonstration and further insights into building a password strength checker in Python, you might find the following video helpful:
 
