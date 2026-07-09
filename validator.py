"""
validator.py
------------
This module validates passwords before they are stored.

Rules:
1. Minimum 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character

It also calculates the password strength.
"""

import re


def validate_password(password):
    """
    Validates the password according to predefined rules.

    Returns:
        (True, "Password is valid")
        OR
        (False, "Reason why password is invalid")
    """

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password):
        return False, "Password must contain at least one special character."

    return True, "Password is valid."


def password_strength(password):
    """
    Returns:
        Weak
        Medium
        Strong
    """

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score == 3 or score == 4:
        return "Medium"

    else:
        return "Strong"


if __name__ == "__main__":

    sample = input("Enter Password: ")

    valid, message = validate_password(sample)

    print(message)

    print("Strength:", password_strength(sample))