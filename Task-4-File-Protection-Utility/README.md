# 🔒 File Protection Utility

## 📌 Overview

The **File Protection Utility** is a Python-based cybersecurity tool that securely encrypts and decrypts sensitive files using password-based encryption. The application implements **PBKDF2 (Password-Based Key Derivation Function 2)** with a randomly generated salt to derive a secure encryption key and performs authenticated symmetric encryption to protect file confidentiality and integrity.

This project demonstrates secure file protection techniques commonly used in cybersecurity and data security applications.

---

## 🎯 Features

- ✅ Password-based file encryption
- ✅ Secure key derivation using **PBKDF2-HMAC-SHA256**
- ✅ Random salt generation for every encryption
- ✅ Symmetric encryption of files
- ✅ File decryption using the correct password
- ✅ Integrity verification during decryption
- ✅ Generates encrypted `.enc` files
- ✅ Command-line interface
- ✅ Protects sensitive local files

---

## 🛠 Technologies Used

- Python 3
- cryptography library
- PBKDF2-HMAC-SHA256
- Symmetric Encryption

---

## 📂 Project Structure

```text
Task-4-File-Protection-Utility/
│
├── FileProtectionUtility.py
├── sample.txt
├── README.md
└── screenshots/
    ├── encrypt.png
    ├── decrypt.png
    ├── wrong_password.png
    └── files.png
```

---

## ⚙️ How It Works

The utility performs the following steps:

1. Accepts a file name from the user.
2. Accepts a password securely.
3. Generates a random salt.
4. Derives a secure encryption key using **PBKDF2-HMAC-SHA256**.
5. Encrypts the selected file.
6. Saves the encrypted file with a **`.enc`** extension.
7. Decrypts the encrypted file using the same password.
8. Verifies the integrity of the encrypted data before decryption.

---

## 🔐 Security Features

- AES-based authenticated symmetric encryption
- PBKDF2-HMAC-SHA256 key derivation
- Random 16-byte salt generation
- Password-based encryption
- Integrity verification
- Protection against incorrect passwords
- Secure encrypted file storage

---

## ▶️ Installation

Install the required dependency:

```bash
pip install cryptography
```

---

## ▶️ How to Run

Run the program:

```bash
python FileProtectionUtility.py
```

Choose an option:

```
1. Encrypt File
2. Decrypt File
```

Enter the file name and password when prompted.

---

## 💻 Sample Encryption Output

```text
=======================================================
        FILE PROTECTION UTILITY
=======================================================

1. Encrypt File
2. Decrypt File

Enter choice: 1
Enter file name: sample.txt
Enter password:

Encryption Successful
Encrypted File: sample.txt.enc
```

---

## 💻 Sample Decryption Output

```text
=======================================================
        FILE PROTECTION UTILITY
=======================================================

1. Encrypt File
2. Decrypt File

Enter choice: 2
Enter file name: sample.txt.enc
Enter password:

Decryption Successful
Output File: sample_decrypted.txt
```

---

## 💻 Incorrect Password Output

```text
Incorrect password or corrupted file.
```

---

## 📸 Screenshots

The **screenshots/** folder contains execution logs demonstrating:

- Encryption process
- Decryption process
- Incorrect password handling
- Generated encrypted file

Example:

```markdown
### Encryption
![Encryption](screenshots/encrypt.png)

### Decryption
![Decryption](screenshots/decrypt.png)

### Wrong Password
![Wrong Password](screenshots/wrong_password.png)

### Generated Files
![Files](screenshots/files.png)
```

---

## 🔒 Security Concepts Demonstrated

- Password-Based Encryption
- PBKDF2 Key Derivation
- Random Salt Generation
- Symmetric Encryption
- Secure File Storage
- Authentication & Integrity Verification
- Confidentiality of Sensitive Data

---

## 🎓 Learning Outcomes

Through this project, I learned:

- Secure password-based encryption techniques.
- How PBKDF2 strengthens password security.
- The importance of random salts in preventing attacks.
- File encryption and decryption workflows.
- Protecting sensitive data using Python.
- Best practices for secure file handling.

---

## ⚠️ Disclaimer

This project was developed **for educational purposes** as part of the **Workora Cybersecurity Internship**. It should only be used to protect files you own or are authorized to manage.

---

## 📜 License

This project is intended for educational and learning purposes under the **Workora Cybersecurity Internship Program**.
