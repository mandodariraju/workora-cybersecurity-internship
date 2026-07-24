# 🔐 Cryptographic Encryption Vault

## 📌 Overview

The **Cryptographic Encryption Vault** is a Python-based cybersecurity tool designed to securely encrypt and decrypt entire directories containing multiple files.

The application uses secure cryptographic techniques to protect sensitive data by applying authenticated encryption, password-based key derivation, and secure key backup management.

This project demonstrates secure file storage and data protection practices used in cybersecurity applications.

---

# 🎯 Objective

The objective of this project is to build a secure directory encryption system that:

- Encrypts multiple files recursively
- Protects sensitive information using a master password
- Generates secure encryption keys
- Restores encrypted files without data corruption
- Maintains confidentiality and integrity of stored data

---

# ✨ Features

- ✅ Recursive directory scanning
- ✅ Multi-file encryption
- ✅ Password-based encryption
- ✅ PBKDF2-HMAC-SHA256 key derivation
- ✅ Secure random salt generation
- ✅ Fernet authenticated encryption
- ✅ Key backup generation
- ✅ Directory restoration
- ✅ Data integrity verification
- ✅ Command-line interface

---

# 🛠 Technologies Used

- Python 3
- Cryptography Library
- Fernet Symmetric Encryption
- PBKDF2-HMAC-SHA256
- File System Operations

---

# 📂 Project Structure

```text
Task-6-Cryptographic-Encryption-Vault/
│
├── CryptoVault.py
├── vault_key_backup.key
├── Test_Vault/
│   ├── file1.txt
│   └── file2.txt
│
├── README.md
│
└── screenshots/
    ├── encryption.png
    ├── decryption.png
    └── restored_files.png
