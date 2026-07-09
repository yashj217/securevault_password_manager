"""
auth.py
--------
Handles user registration and login.

Features:
1. Register User
2. Login User
3. Stores users in JSON
4. Password Hashing using bcrypt
"""

import json
import os
import bcrypt

from validator import validate_password

USER_FILE = "data/users.json"

MAX_ATTEMPTS = 3

def ensure_user_file():

    if not os.path.exists(USER_FILE):

        with open(USER_FILE,"w") as file:

            json.dump([],file,indent=4)

def load_users():

    ensure_user_file()

    with open(USER_FILE,"r") as file:

        return json.load(file)     

def save_users(users):

    with open(USER_FILE,"w") as file:

        json.dump(users,file,indent=4)           

def register():
    """
    Registers a new user.
    """

    users = load_users()

    print("\n========== REGISTER ==========")

    username = input("Enter Username: ").strip()

    # Check if username already exists
    for user in users:
        if user["username"].lower() == username.lower():
            print("❌ Username already exists.")
            return
#stops the loop
    while True:
#keeps user asking the password untill the correct is told
        password = input("Enter Password: ").strip()

        valid, message = validate_password(password)
#valid returns true or false and message returns as mention inthe validator module
        if not valid:
            print(f"❌ {message}")
            continue

        confirm_password = input("Confirm Password: ").strip()

        if password != confirm_password:
            print("❌ Passwords do not match.")
            continue

        break

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    users.append({
        "username": username,
        "password": hashed_password
    })

    save_users(users)

    print("✅ Registration Successful!")        



    def login():
     """
    Authenticates an existing user.
    Returns True if login is successful, otherwise False.
    """

    users = load_users()

    print("\n========== LOGIN ==========")

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        for user in users:

            if user["username"].lower() == username.lower():

                if bcrypt.checkpw(
                    password.encode(),
                    user["password"].encode()
                ):

                    print(f"\n✅ Welcome, {username}!")
                    return True

                break

        attempts += 1

        remaining = MAX_ATTEMPTS - attempts

        if remaining > 0:
            print(f"❌ Invalid Username or Password. Attempts Left: {remaining}")

        else:
            print("❌ Maximum Login Attempts Reached.")

    return False