# 🔐 Password Strength Checker

## 📌 Overview

The **Password Strength Checker** is a Python-based cybersecurity project that evaluates the strength of a password using **security policy validation**, **entropy calculations**, and **dictionary password detection**.

The program analyzes a password against common security requirements and provides a strength classification along with recommendations to improve password security.

---

## 🎯 Features

- ✅ Checks minimum password length
- ✅ Verifies uppercase letters
- ✅ Verifies lowercase letters
- ✅ Checks for numeric digits
- ✅ Detects special characters
- ✅ Calculates password entropy
- ✅ Detects common weak (dictionary) passwords
- ✅ Classifies password strength:
  - Weak
  - Moderate
  - Strong
  - Exceptional
- ✅ Provides actionable security suggestions

---

## 🛠 Technologies Used

- Python 3
- math module
- string module

---

## 📂 Project Structure

```
Password-Strength-Checker/
│
├── PasswordStrengthChecker.py
├── README.md
└── screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

---

## ⚙️ How It Works

The program performs the following checks:

1. Validates password length (minimum 8 characters)
2. Checks for:
   - Uppercase letters
   - Lowercase letters
   - Digits
   - Special characters
3. Calculates password entropy using:

```
Entropy = Password Length × log₂(Character Set Size)
```

4. Compares the password against a list of commonly used weak passwords.
5. Assigns a strength level based on:
   - Security policy compliance
   - Entropy score
   - Dictionary password detection
6. Provides suggestions for improving password security.

---

## 📊 Password Strength Classification

| Entropy (bits) | Strength |
|---------------|----------|
| < 40 | Weak |
| 40 – 59 | Moderate |
| 60 – 79 | Strong |
| ≥ 80 | Exceptional |

**Note:** Any password found in the common password list is automatically classified as **Weak**.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/Password-Strength-Checker.git
```

Navigate to the project folder:

```bash
cd Password-Strength-Checker
```

Run the program:

```bash
python PasswordStrengthChecker.py
```

---

## 💻 Sample Output

```
==================================================
        PASSWORD STRENGTH CHECKER
==================================================

Enter your password: Secure@123

Password Analysis
--------------------------------------------------
Length              : Yes
Uppercase           : Yes
Lowercase           : Yes
Digits              : Yes
Special Characters  : Yes

Password Entropy : 65.55 bits
Password Strength: Strong

Excellent! Your password follows recommended security practices.
```

---

## 📸 Screenshots

Screenshots of the program execution are available in the **screenshots/** folder.

- output1.png
- output2.png
- output3.png

---

## 🔒 Security Concepts Demonstrated

- Password Policy Validation
- Password Entropy Calculation
- Dictionary Password Detection
- Password Strength Classification
- Secure Password Recommendations

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Password security best practices
- Entropy-based password evaluation
- Implementing password policy validation
- Detecting weak and common passwords
- Building a Python command-line cybersecurity utility

---

## 📜 License

This project is developed for educational purposes as part of a **Cybersecurity Internship Task**.
