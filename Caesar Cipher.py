def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep symbols/spaces unchanged
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main function
if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool")
    choice = input("Type (e)ncrypt or (d)ecrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift number (e.g. 3): "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("🔒 Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("🔓 Decrypted message:", decrypted)
    else:
        print("❌ Invalid option. Choose 'e' or 'd'.")
