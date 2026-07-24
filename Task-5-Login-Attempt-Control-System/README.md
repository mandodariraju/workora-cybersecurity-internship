# 🔐 Login Attempt Control System

## 📌 Overview

The **Login Attempt Control System** is a Python-based cybersecurity utility designed to prevent brute-force attacks by monitoring failed login attempts and enforcing account lockout mechanisms.

The system tracks authentication failures, applies progressive delays, temporarily locks accounts after multiple failed attempts, and maintains security logs for administrative auditing.

---

## 🎯 Objective

The objective of this project is to implement a secure authentication control mechanism that protects user accounts against repeated unauthorized login attempts.

The system demonstrates:

- Failed login tracking
- Rate limiting
- Temporary account lockout
- Brute-force attack simulation
- Security event logging

---

## ✨ Features

- ✅ Username-based failed login tracking
- ✅ IP address tracking
- ✅ Failed login attempt counter
- ✅ Progressive delay after failed attempts
- ✅ Account lockout after 5 consecutive failures
- ✅ 15-minute temporary lockout mechanism
- ✅ Security audit log generation
- ✅ Brute-force attack simulation
- ✅ Command-line interface

---

## 🛠 Technologies Used

- Python 3
- datetime module
- time module
- File handling
- Authentication security concepts

---

## 📂 Project Structure

```text
Task-5-Login-Attempt-Control-System/
│
├── LoginAttemptControl.py
├── security_log.txt
├── README.md
└── screenshots/
    ├── failed_attempts.png
    ├── account_locked.png
    └── security_log.png
