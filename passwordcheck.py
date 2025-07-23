import re

def password_check(password):
    # Check minimum length
    if len(password) < 8:
        return "❌ Password must be at least 8 characters long."

    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        return "❌ Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        return "❌ Password must contain at least one lowercase letter."

    # Check for digit
    if not re.search(r"[0-9]", password):
        return "❌ Password must contain at least one digit."

    # Check for special character
    if not re.search(r"[!@#$%^&*()\-_=+]", password):
        return "❌ Password must contain at least one special character (!@#$%^&*()-_+=)."

    return "✅ Password is strong!"

# Main program
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter your password: ")
    result = password_check(user_password)
    print(result)
