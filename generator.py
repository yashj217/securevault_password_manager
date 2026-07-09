"""
generator.py
-------------
Generates secure random passwords.
"""

import secrets
import string


def generate_password(length=12):
    """
    Generates a secure random password.

    Default length = 12
    """

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    all_characters = lowercase + uppercase + digits + symbols

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print(generate_password())