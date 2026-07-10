"""
password_manager.py
-------------------
Handles all password management operations.

Features:
1. Add Password
2. View Passwords
3. Search Password
4. Update Password
5. Delete Password

Passwords are:
• Stored inside passwords.json
• Encrypted using Fernet
• Linked to the logged-in user
"""

import os
import json
from datetime import datetime

from encryption import encrypt_password, decrypt_password
from validator import validate_password

PASSWORD_FILE = "data/passwords.json"


def ensure_password_file():
    """
    Creates passwords.json if it does not exist.
    """

    if not os.path.exists(PASSWORD_FILE):

        with open(PASSWORD_FILE, "w") as file:
#[] inside the file meaning empty list
            json.dump([], file, indent=4)


def load_passwords():
    """
    Reads all password records from passwords.json.
    Returns a list.
    """

    ensure_password_file()

    with open(PASSWORD_FILE, "r") as file:

        return json.load(file)


def save_passwords(passwords):
    """
    Saves all password records to passwords.json.
    """

    with open(PASSWORD_FILE, "w") as file:

        json.dump(passwords, file, indent=4)


def add_password(current_user):
    """
    Adds a new password for the logged-in user.
    """

    passwords = load_passwords()

    print("\n========== ADD PASSWORD ==========")

    website = input("Enter Website Name: ").strip()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if not website or not username or not password:
        print("❌ All fields are required.")
        return

    valid, message = validate_password(password)

    if not valid:
        print(f"❌ {message}")
        return

    encrypted_password = encrypt_password(password)

    passwords.append({

        "owner": current_user,

        "website": website,

        "username": username,

        "password": encrypted_password,

        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#strfrmt means stringformat tieme
    })

    save_passwords(passwords)

    print("✅ Password Added Successfully.")       

def view_passwords(current_user):
    """
    Displays all passwords of the logged-in user.
    """

    passwords = load_passwords()

    print("\n========== SAVED PASSWORDS ==========")

    found = False

    for record in passwords:

        if record["owner"] == current_user:

            print(f"\nWebsite    : {record['website']}")
            print(f"Username   : {record['username']}")
            print(f"Password   : {decrypt_password(record['password'])}")
            print(f"Created At : {record['created_at']}")

            found = True

    if not found:
        print("❌ No Passwords Found.")   

def search_password(current_user):
    """
    Searches a password by website.
    """

    passwords = load_passwords()

    website = input("Enter Website Name: ").strip()

    found = False

    for record in passwords:

        if (
            record["owner"] == current_user
            and record["website"].lower() == website.lower()
        ):

            print(f"\nWebsite    : {record['website']}")
            print(f"Username   : {record['username']}")
            print(f"Password   : {decrypt_password(record['password'])}")
            print(f"Created At : {record['created_at']}")

            found = True
            break

    if not found:
        print("❌ Password Not Found.")     

def update_password(current_user):
    """
    Updates an existing password.
    """

    passwords = load_passwords()

    website = input("Enter Website Name: ").strip()

    for record in passwords:

        if (
            record["owner"] == current_user
            and record["website"].lower() == website.lower()
        ):

            new_password = input("Enter New Password: ").strip()

            valid, message = validate_password(new_password)

            if not valid:
                print(f"❌ {message}")
                return

            record["password"] = encrypt_password(new_password)

            save_passwords(passwords)

            print("✅ Password Updated Successfully.")

            return

    print("❌ Website Not Found.")       

def delete_password(current_user):
     """
    Deletes a saved password.
    """

     passwords = load_passwords()

     website = input("Enter Website Name: ").strip()

     updated_passwords = []
#creates a new list which will contain the new password and will remove the password whaich was to be deleted
     found = False

     for record in passwords:

        if (
            record["owner"] == current_user
            and record["website"].lower() == website.lower()
        ):

            found = True
            continue

        updated_passwords.append(record)

     if found:

        save_passwords(updated_passwords)

        print("✅ Password Deleted Successfully.")

     else:

        print("❌ Website Not Found.")      