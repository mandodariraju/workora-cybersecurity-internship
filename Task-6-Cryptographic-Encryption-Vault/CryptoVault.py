import os
import base64
import getpass
import shutil

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# -------------------------------
# Key Generation using PBKDF2
# -------------------------------

def generate_key(password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    return base64.urlsafe_b64encode(
        kdf.derive(password.encode())
    )


# -------------------------------
# Create Key Backup
# -------------------------------

def create_key_backup(key):

    with open("vault_key_backup.key", "wb") as file:
        file.write(key)

    print("Key backup created: vault_key_backup.key")


# -------------------------------
# Encrypt Directory
# -------------------------------

def encrypt_directory(folder, password):

    salt = os.urandom(16)

    key = generate_key(
        password,
        salt
    )

    cipher = Fernet(key)


    create_key_backup(key)


    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(
                root,
                file
            )


            with open(path, "rb") as f:
                data = f.read()


            encrypted = cipher.encrypt(data)


            with open(
                path + ".enc",
                "wb"
            ) as f:

                f.write(
                    salt + encrypted
                )


            os.remove(path)


            print(
                "Encrypted:",
                path
            )


    print("\nDirectory Encryption Completed!")


# -------------------------------
# Decrypt Directory
# -------------------------------

def decrypt_directory(folder, password):


    for root, dirs, files in os.walk(folder):

        for file in files:


            if file.endswith(".enc"):


                path = os.path.join(
                    root,
                    file
                )


                with open(path,"rb") as f:

                    data = f.read()


                salt = data[:16]

                encrypted = data[16:]


                key = generate_key(
                    password,
                    salt
                )


                cipher = Fernet(key)


                try:

                    decrypted = cipher.decrypt(
                        encrypted
                    )


                    new_file = path.replace(
                        ".enc",
                        ""
                    )


                    with open(
                        new_file,
                        "wb"
                    ) as f:

                        f.write(
                            decrypted
                        )


                    os.remove(path)


                    print(
                        "Restored:",
                        new_file
                    )


                except:

                    print(
                        "Wrong password:",
                        file
                    )


    print("\nDirectory Restoration Completed!")



# -------------------------------
# Main Program
# -------------------------------

def main():

    print("="*60)
    print("        CRYPTOGRAPHIC ENCRYPTION VAULT")
    print("="*60)


    print("""
1. Encrypt Directory
2. Decrypt Directory
""")


    choice=input(
        "Enter choice: "
    )


    folder=input(
        "Enter folder path: "
    )


    password=getpass.getpass(
        "Enter master password: "
    )


    if choice=="1":

        encrypt_directory(
            folder,
            password
        )


    elif choice=="2":

        decrypt_directory(
            folder,
            password
        )


    else:

        print("Invalid choice")



if __name__=="__main__":
    main()
