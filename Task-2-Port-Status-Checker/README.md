# 🌐 Port Status Checker

## 📌 Overview

The **Port Status Checker** is a Python-based cybersecurity tool that scans a target host to determine the status of TCP ports. It uses Python's built-in **socket** library to perform TCP connection handshakes and identify whether ports are **Open**, **Closed**, or **Filtered**.

This project demonstrates the fundamentals of network socket programming and basic port scanning techniques used in network security assessments.

---

## 🎯 Features

- ✅ Accepts a target IP address
- ✅ Accepts a user-defined port range
- ✅ Performs TCP connection attempts using sockets
- ✅ Uses configurable timeout values
- ✅ Detects Open, Closed, and Filtered ports
- ✅ Displays results in a formatted table
- ✅ Calculates and displays total scan time
- ✅ Simple command-line interface

---

## 🛠 Technologies Used

- Python 3
- socket module
- time module

---

## 📂 Project Structure

```
Task-2-Port-Status-Checker/
│
├── PortStatusChecker.py
├── README.md
└── screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

---

## ⚙️ How It Works

The program follows these steps:

1. Imports the required Python libraries.
2. Accepts a target IP address from the user.
3. Accepts the starting and ending port numbers.
4. Creates a TCP socket for each port.
5. Attempts a TCP connection with a specified timeout.
6. Determines whether the port is:
   - Open
   - Closed
   - Filtered
7. Displays the scan results in a formatted table.
8. Calculates and displays the total scanning time.

---

## 📊 Port Status Classification

| Status | Description |
|---------|-------------|
| 🟢 Open | The target host accepted the TCP connection. |
| 🔴 Closed | The target host responded that the port is closed. |
| 🟡 Filtered | The connection timed out or was blocked by a firewall. |

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Task-2-Port-Status-Checker.git
```

### Navigate to the project folder

```bash
cd Task-2-Port-Status-Checker
```

### Run the program

```bash
python PortStatusChecker.py
```

---

## 💻 Sample Output

```
============================================================
            PORT STATUS CHECKER
============================================================

Enter Target IP Address: 127.0.0.1
Enter Starting Port: 20
Enter Ending Port: 30

Scanning...
------------------------------------------------------------

PORT       STATUS
------------------------------------------------------------
20         Closed
21         Closed
22         Open
23         Closed
24         Closed
25         Closed
26         Closed
27         Closed
28         Closed
29         Closed
30         Closed

------------------------------------------------------------
Scan completed in 0.45 seconds.
```

---

## 📸 Screenshots

The **screenshots/** folder contains execution logs of the program.

- output1.png
- output2.png
- output3.png

To display them in this README:

```markdown
### Output 1
![Output 1](screenshots/output1.png)

### Output 2
![Output 2](screenshots/output2.png)

### Output 3
![Output 3](screenshots/output3.png)
```

---

## 🔒 Security Concepts Demonstrated

- Socket Programming
- TCP Connection Handshake
- Port Scanning
- Network Service Discovery
- Timeout Handling
- Basic Network Enumeration

---

## 🎓 Learning Outcomes

Through this project, I learned:

- How TCP socket communication works.
- How to use Python's socket library.
- How port scanning is performed.
- How to identify open, closed, and filtered ports.
- How to build a basic network auditing utility.
- Safe and ethical practices for network scanning.

---

## ⚠️ Disclaimer

This tool is intended **for educational purposes only**. Use it only on systems you own or have explicit permission to test. Unauthorized port scanning of third-party systems may violate laws, regulations, or organizational policies.

---

## 📜 License

This project was developed as part of a **Cybersecurity Internship Task** for educational and learning purposes.
