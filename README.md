# 🛡️ Workora Cybersecurity Internship Projects

## 📌 Overview

This repository contains the cybersecurity projects completed as part of the **Workora Cybersecurity Internship Program**.

The projects focus on practical implementation of cybersecurity concepts including password security, network scanning, phishing detection, encryption, authentication security, and network traffic analysis.

Each task demonstrates hands-on programming, security concepts, and implementation of defensive security tools using Python.

---

# 📂 Project Structure

```text
workora-cybersecurity-internship/
│
├── Task-1-Password-Strength-Checker/
│   ├── PasswordStrengthChecker.py
│   ├── README.md
│   └── screenshots/
│
├── Task-2-Port-Status-Checker/
│   ├── PortStatusChecker.py
│   ├── README.md
│   └── screenshots/
│
├── Task-3-Email-Risk-Analyzer/
│   ├── EmailRiskAnalyzer.py
│   ├── sample_email.txt
│   ├── Email_Phishing_Analysis_Report.pdf
│   ├── README.md
│   └── screenshots/
│
├── Task-4-File-Protection-Utility/
│   ├── FileProtectionUtility.py
│   ├── README.md
│   └── screenshots/
│
├── Task-5-Login-Attempt-Control-System/
│   ├── LoginAttemptControl.py
│   ├── security_log.txt
│   ├── README.md
│   └── screenshots/
│
├── Task-6-Cryptographic-Encryption-Vault/
│   ├── CryptoVault.py
│   ├── vault_key_backup.key
│   ├── README.md
│   └── screenshots/
│
├── Task-7-Network-Packet-Sniffer/
│   ├── PacketSniffer.py
│   ├── network_log.txt
│   ├── README.md
│   └── screenshots/
│
└── README.md
# 🚀 Completed Cybersecurity Tasks


# 🔐 Task 1: Password Strength Checker

## 📌 Description

A Python-based password security evaluation tool that analyzes password strength based on security policies and entropy calculations.

The tool evaluates password complexity and provides recommendations to improve password security.

## 🎯 Objectives

- Implement password security validation
- Calculate password entropy
- Identify weak credentials
- Provide security improvement suggestions

## ✨ Features

- Password length verification
- Uppercase character detection
- Lowercase character detection
- Number validation
- Special character checking
- Entropy calculation
- Common password detection
- Strength classification

## 🔧 Technologies Used

- Python
- Math Library
- String Operations

---

# 🌐 Task 2: Port Status Checker

## 📌 Description

A network socket utility developed to check open ports and service availability on a target system.

The tool performs TCP connection tests to identify accessible and closed ports.

## 🎯 Objectives

- Understand socket programming
- Perform port scanning
- Analyze network service availability

## ✨ Features

- Target host scanning
- Port range checking
- TCP handshake testing
- Timeout handling
- Open/Closed port identification

## 🔧 Technologies Used

- Python
- Socket Programming

---

# 📧 Task 3: Email Risk Analyzer

## 📌 Description

A phishing analysis tool that scans email headers and message content to identify possible phishing indicators.

The system evaluates suspicious patterns and generates a risk assessment report.

## 🎯 Objectives

- Detect phishing indicators
- Analyze suspicious email behavior
- Identify spoofing attempts

## ✨ Features

- Email header parsing
- Return-Path analysis
- SPF/DKIM indicator checking
- Suspicious URL detection
- Urgent keyword analysis
- Risk score generation
- Phishing report generation

## 🔧 Technologies Used

- Python
- Email Analysis Techniques
- Security Reporting

---

# 🔒 Task 4: File Protection Utility

## 📌 Description

A secure file encryption and decryption utility designed to protect sensitive files using symmetric encryption.

The application uses password-based key derivation and authenticated encryption.

## 🎯 Objectives

- Implement secure file encryption
- Protect confidential data
- Verify file integrity after decryption

## ✨ Features

- AES-based symmetric encryption
- PBKDF2 key derivation
- Secure random salt generation
- File encryption into `.enc`
- File restoration
- Password verification

## 🔧 Technologies Used

- Python
- Cryptography Library
- Fernet Encryption

---

# 🔑 Task 5: Login Attempt Control System

## 📌 Description

An authentication security mechanism that prevents brute-force attacks by monitoring failed login attempts and applying account lockout policies.

## 🎯 Objectives

- Implement login security controls
- Prevent repeated unauthorized access attempts
- Maintain authentication logs

## ✨ Features

- Failed login counter
- Username tracking
- IP address tracking
- Progressive delay mechanism
- Account lock after 5 failures
- 15-minute temporary lockout
- Security audit logging
- Brute-force attack simulation

## 🔧 Technologies Used

- Python
- Authentication Security Concepts
- File Logging

---

# 🗄️ Task 6: Cryptographic Encryption Vault

## 📌 Description

A directory encryption system that securely encrypts and decrypts multiple files using cryptographic techniques.

The tool protects complete folders while maintaining data integrity.

## 🎯 Objectives

- Implement directory-level encryption
- Secure multiple files
- Manage encryption keys safely

## ✨ Features

- Recursive directory scanning
- Multi-file encryption
- Password-based encryption
- PBKDF2 key generation
- Secure key backup creation
- File restoration
- Data integrity verification

## 🔧 Technologies Used

- Python
- Cryptography Library
- Fernet Encryption

---

# 🌐 Task 7: Network Packet Sniffer

## 📌 Description

A command-line network monitoring tool that captures and analyzes network packets using raw sockets.

The tool extracts protocol information and generates network traffic logs.

## 🎯 Objectives

- Understand packet-level communication
- Analyze network protocols
- Monitor network traffic

## ✨ Features

- Raw socket packet capture
- IP header parsing
- Source IP extraction
- Destination IP extraction
- TCP packet analysis
- UDP packet analysis
- Port number extraction
- Network traffic logging

## 🔧 Technologies Used

- Python
- Socket Programming
- Network Protocol Analysis

---

# ⚙️ Installation & Setup

## Requirements

- Python 3.x
- Windows/Linux/Kali Linux

Check Python installation:

```bash
python --version
```

---

## Install Required Libraries

For encryption-based tasks:

```bash
pip install cryptography
```

Other projects use Python built-in modules.

---

# ▶️ Running the Projects

Navigate to the required task folder and execute:

Example:

```bash
python PasswordStrengthChecker.py
```

```bash
python PortStatusChecker.py
```

```bash
python EmailRiskAnalyzer.py
```

```bash
python FileProtectionUtility.py
```

```bash
python LoginAttemptControl.py
```

```bash
python CryptoVault.py
```

```bash
python PacketSniffer.py
```

---

# 📸 Project Evidence

Each task folder contains:

- Python source code
- README documentation
- Execution screenshots
- Output logs
- Reports (where applicable)

These files demonstrate successful implementation and testing of each cybersecurity utility.

---

# 🧠 Skills & Concepts Learned

Through these projects, I gained practical knowledge in:

## Programming

- Python scripting
- File handling
- Error handling
- Command-line utilities

## Cybersecurity

- Password security
- Authentication protection
- Brute-force prevention
- Phishing detection
- Cryptographic security
- Network monitoring
- Packet analysis

## Networking

- Socket programming
- TCP/UDP protocols
- IP addressing
- Network traffic inspection

## Security Tools & Concepts

- Encryption mechanisms
- Key management
- Security logging
- Defensive security practices

---

# ⚠️ Disclaimer

These projects were developed for **educational purposes only** as part of the **Workora Cybersecurity Internship Program**.

The tools should only be used on systems, networks, and files where proper authorization has been provided.

Unauthorized access, monitoring, or testing of systems may violate security policies and legal regulations.

---

# 📜 License

This repository is created for educational and cybersecurity learning purposes.
