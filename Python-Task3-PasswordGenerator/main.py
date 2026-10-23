
import secrets
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+?"

    if not characters:
        return None

    if length < 4 or length > 128:
        return None

    password = []

    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice("!@#$%^&*()-_=+?"))

    remaining = length - len(password)
    password.extend(
        secrets.choice(characters) for _ in range(remaining)
    )

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


print("=" * 42)
print("       RANDOM PASSWORD GENERATOR")
print("=" * 42)

try:
    length = int(input("Password length (4-128): "))

    if not 4 <= length <= 128:
        print("Please enter a length between 4 and 128.")
    else:
        upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        digits = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(
            length, upper, lower, digits, symbols
        )

        if password:
            print("\nGenerated password:", password)
            print("Password length:", len(password))
        else:
            print("Select at least one character type.")

except ValueError:
    print("Invalid input! Enter a number for password length.")

print("\nKeep your password private!")
