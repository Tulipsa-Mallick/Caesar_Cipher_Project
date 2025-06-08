def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces, punctuation unchanged

    return result

# Main interaction
if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    text = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    action = input("Type 'encrypt' or 'decrypt': ").strip().lower()

    if action in ['encrypt', 'decrypt']:
        output = caesar_cipher(text, shift, action)
        print(f"Result: {output}")
    else:
        print("Invalid action selected.")
