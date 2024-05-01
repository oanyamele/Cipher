import sys

def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            char = char.upper()
            encoded_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encoded_message += encoded_char
    return encoded_message

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py 2")
        return
    try:
        shift_amount = int(sys.argv[1]) % 26
    except ValueError:
        print("The shift amount entered is invalid.")
        return

    message = sys.stdin.readline().strip()

    encoded_message = encode_message(message, shift_amount)

    for i in range(0, len(encoded_message), 5):
        print(encoded_message[i:i+5], end=" ")


main()



