import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 for better security!")
        return None
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
