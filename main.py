"""
main.py
-------
Entry point of SecureVault Password Manager.

Flow:
1. Welcome Screen
2. Register / Login
3. Password Manager Menu
"""

from auth import register, login
from password_manager import (
    add_password,
    view_passwords,
    search_password,
    update_password,
    delete_password,
)
from backup import backup_passwords, restore_passwords
from generator import generate_password


def show_main_menu():
    """
    Displays the login menu.
    """
    print("\n" + "=" * 45)
    print("      SECUREVAULT PASSWORD MANAGER")
    print("=" * 45)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=" * 45)


def show_password_menu():
    """
    Displays the password manager menu.
    """
    print("\n" + "=" * 45)
    print("          PASSWORD MANAGER")
    print("=" * 45)
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Generate Strong Password")
    print("7. Backup Passwords")
    print("8. Restore Passwords")
    print("9. Logout")
    print("=" * 45)


def password_manager():

    while True:

        show_password_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            search_password()

        elif choice == "4":
            update_password()

        elif choice == "5":
            delete_password()

        elif choice == "6":

            password = generate_password()

            print("\nGenerated Password:", password)

        elif choice == "7":
            backup_passwords()

        elif choice == "8":
            restore_passwords()

        elif choice == "9":

            print("Logged Out Successfully.")

            break

        else:

            print("Invalid Choice.")


def main():

    while True:

        show_main_menu()

        choice = input("Enter Choice: ").strip()

        if choice == "1":

            register()

        elif choice == "2":

            if login():

                password_manager()

        elif choice == "3":

            print("Thank You For Using SecureVault.")

            break

        else:

            print("Invalid Choice.")


if __name__ == "__main__":
    main()