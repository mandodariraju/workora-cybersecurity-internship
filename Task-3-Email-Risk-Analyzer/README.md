# 📧 Email Risk Analyzer

## 📌 Overview

The **Email Risk Analyzer** is a Python-based cybersecurity tool designed to analyze email headers and body content for potential phishing and spoofing attempts. The program examines common email authentication headers, detects suspicious links and phishing-related keywords, assigns a risk score, and generates a security assessment to help identify potentially malicious emails.

This project demonstrates the fundamentals of email security analysis and phishing detection techniques.

---

## 🎯 Features

- ✅ Parses raw email headers
- ✅ Checks **Received**, **Return-Path**, **SPF**, and **DKIM** headers
- ✅ Detects suspicious or missing email authentication records
- ✅ Scans email body for phishing-related keywords
- ✅ Detects suspicious hyperlinks
- ✅ Calculates an overall phishing risk score
- ✅ Classifies emails as:
  - Low Risk
  - Medium Risk
  - High Risk
- ✅ Generates a detailed email security audit report
- ✅ Command-line interface for easy analysis

---

## 🛠 Technologies Used

- Python 3
- email module
- re (Regular Expressions)
- urllib.parse
- os module

---

## 📂 Project Structure

```
Task-3-Email-Risk-Analyzer/
│
├── EmailRiskAnalyzer.py
├── sample_email.txt
├── README.md
├── Email_Phishing_Analysis_Report.pdf
└── screenshots/
    ├── output1.png
    ├── output2.png
    └── report.png
```

---

## ⚙️ How It Works

The analyzer performs the following steps:

1. Reads the raw email file.
2. Parses email headers.
3. Extracts important authentication headers:
   - Received
   - Return-Path
   - SPF
   - DKIM
4. Checks for missing or suspicious authentication results.
5. Scans the email body for:
   - Urgent action keywords
   - Suspicious links
   - Domain spoofing indicators
6. Calculates a phishing risk score.
7. Classifies the email risk level.
8. Generates a detailed security audit report.

---

## 📊 Risk Classification

| Risk Score | Classification |
|------------|----------------|
| 0 – 30 | 🟢 Low Risk |
| 31 – 70 | 🟡 Medium Risk |
| 71 – 100 | 🔴 High Risk |

---

## 🔍 Security Checks Performed

### Header Analysis

- Received Header
- Return-Path
- SPF Status
- DKIM Status

### Body Analysis

- Suspicious URLs
- Phishing Keywords
- Urgent Action Messages
- Spoofing Indicators
- Suspicious Email Content

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Task-3-Email-Risk-Analyzer.git
```

### Navigate to the project folder

```bash
cd Task-3-Email-Risk-Analyzer
```

### Run the program

```bash
python EmailRiskAnalyzer.py
```

---

## 💻 Sample Output

```
====================================================
            EMAIL RISK ANALYZER
====================================================

Header Analysis
-------------------------------
SPF Status       : Failed
DKIM Status      : Missing
Return-Path      : Suspicious

Body Analysis
-------------------------------
Suspicious Links : 2
Urgent Keywords  : 4

Risk Score       : 82/100

Risk Level       : HIGH RISK

Recommendation:
This email is likely a phishing attempt.
Avoid clicking links or downloading attachments.
Verify the sender before responding.
```

---

## 📄 Email Security Audit Report

The program generates a detailed phishing analysis report containing:

- Email Header Analysis
- Authentication Results (SPF/DKIM)
- Suspicious Indicators
- Risk Score
- Risk Classification
- Security Recommendations

Example report file:

```
Email_Phishing_Analysis_Report.pdf
```

---

## 📸 Screenshots

Execution logs and report screenshots are available in the **screenshots/** folder.

To display them in this README:

```markdown
### Program Output
![Output 1](screenshots/output1.png)

### Risk Analysis
![Output 2](screenshots/output2.png)

### Security Report
![Report](screenshots/report.png)
```

---

## 🔒 Security Concepts Demonstrated

- Email Header Analysis
- SPF Validation
- DKIM Verification
- Phishing Detection
- Domain Spoofing Detection
- Suspicious URL Detection
- Email Risk Scoring
- Security Reporting

---

## 🎓 Learning Outcomes

Through this project, I learned:

- How email headers are structured.
- The importance of SPF and DKIM in email authentication.
- Techniques used to detect phishing emails.
- How suspicious links and urgent language are used in social engineering attacks.
- How to automate email security analysis using Python.
- Best practices for identifying potentially malicious emails.

---

## ⚠️ Disclaimer

This project is developed **for educational purposes only**. It is intended to demonstrate email security analysis techniques and should only be used for authorized testing and cybersecurity learning.

---

## 📜 License

This project was developed as part of a **Cybersecurity Internship Task** for educational and learning purposes.
