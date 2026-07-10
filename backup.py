"""
backup.py
---------
Handles backup and restore of password data.
"""

import json
import os
import shutil

PASSWORD_FILE = "data/passwords.json"
BACKUP_FILE = "data/backup.json"


def backup_passwords():
    """
    Creates a backup of passwords.json
    """

    print("\n========== BACKUP PASSWORDS ==========")

    if not os.path.exists(PASSWORD_FILE):
        print("❌ Password file does not exist.")
        return

    try:

        shutil.copyfile(PASSWORD_FILE, BACKUP_FILE)

        print("✅ Backup Created Successfully.")

    except Exception as error:

        print(f"❌ Backup Failed : {error}")


def restore_passwords():
    """
    Restores passwords from backup.
    """

    print("\n========== RESTORE PASSWORDS ==========")

    if not os.path.exists(BACKUP_FILE):
        print("❌ Backup file not found.")
        return

    try:

        shutil.copyfile(BACKUP_FILE, PASSWORD_FILE)

        print("✅ Passwords Restored Successfully.")

    except Exception as error:

        print(f"❌ Restore Failed : {error}")