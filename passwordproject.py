import string
import random
import re

def generate_password(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError('Password length is too short for the specified criteria.')

    password = ''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[0-9]', password):
        strength += 1
    if re.search('[@#$%+=!]', password):
        strength += 1

    return strength


def print_strength_message(strength):
    if strength == 5:
        print('Password strength: Very Strong')
    elif strength == 4:
        print('Password strength: Strong')
    elif strength == 3:
        print('Password strength: Medium')
    elif strength == 2:
        print('Password strength: Weak')
    else:
        print('Password strength: Very Weak')


def main():
    while True:
        print("\n--- Password Utility ---")
        print("1. Generate a password")
        print("2. Check password strength")
        print("3. Generate and check strength")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                length = int(input('Enter password length: '))
                include_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
                include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
                include_special = input('Include special characters? (y/n): ').lower() == 'y'

                password = generate_password(length, include_uppercase, include_numbers, include_special)
                print(f'Generated Password: {password}')
            except ValueError as e:
                print(e)

        elif choice == '2':
            password = input('Enter a password to check: ')
            strength = check_password_strength(password)
            print_strength_message(strength)

        elif choice == '3':
            try:
                length = int(input('Enter password length: '))
                include_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
                include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
                include_special = input('Include special characters? (y/n): ').lower() == 'y'

                password = generate_password(length, include_uppercase, include_numbers, include_special)
                print(f'Generated Password: {password}')
                strength = check_password_strength(password)
                print_strength_message(strength)
            except ValueError as e:
                print(e)

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
