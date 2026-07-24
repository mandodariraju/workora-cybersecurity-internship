import time
from datetime import datetime, timedelta


# User database (demo purpose)
users = {
    "admin": "Admin@123",
    "user": "User@123"
}


# Track login attempts
login_data = {}


MAX_ATTEMPTS = 5
LOCK_TIME = 15 * 60   # 15 minutes


# Logging function
def write_log(message):

    with open("security_log.txt", "a") as file:
        timestamp = datetime.now()

        file.write(
            f"[{timestamp}] {message}\n"
        )


# Check account lock status
def is_locked(username):

    if username in login_data:

        if "lock_until" in login_data[username]:

            if datetime.now() < login_data[username]["lock_until"]:
                return True

            else:
                del login_data[username]["lock_until"]

    return False



# Login authentication
def login(username, password, ip):


    if username not in login_data:

        login_data[username] = {
            "failed": 0,
            "ip": ip
        }


    # Check lock
    if is_locked(username):

        print("\nAccount Locked!")
        print("Try again after 15 minutes.")

        return False



    # Correct password
    if username in users and users[username] == password:


        print("\nLogin Successful!")

        login_data[username]["failed"] = 0

        write_log(
            f"Successful login: {username} from IP {ip}"
        )

        return True



    # Failed attempt
    login_data[username]["failed"] += 1


    attempts = login_data[username]["failed"]


    print(
        f"\nInvalid password!"
        f" Failed Attempts: {attempts}/{MAX_ATTEMPTS}"
    )


    write_log(
        f"Failed login attempt: {username} "
        f"IP:{ip} Attempt:{attempts}"
    )


    # Lock account
    if attempts >= MAX_ATTEMPTS:


        login_data[username]["lock_until"] = (
            datetime.now()
            +
            timedelta(seconds=LOCK_TIME)
        )


        print(
            "\nToo many failed attempts!"
        )

        print(
            "Account locked for 15 minutes."
        )


        write_log(
            f"ACCOUNT LOCKED: {username} "
            f"IP:{ip}"
        )


    else:

        delay = attempts * 2

        print(
            f"Security delay: {delay} seconds"
        )

        time.sleep(delay)


    return False



# Brute force simulation
def brute_force_test():

    print("\n--- Brute Force Attack Simulation ---")


    for i in range(6):

        print(
            f"\nAttack Attempt {i+1}"
        )

        login(
            "admin",
            "wrongpassword",
            "192.168.1.10"
        )



# Main program
def main():

    print("="*60)
    print("     LOGIN ATTEMPT CONTROL SYSTEM")
    print("="*60)


    print("""
1. Normal Login
2. Simulate Brute Force Attack
""")


    choice = input(
        "Enter choice: "
    )


    if choice == "1":

        username = input(
            "Username: "
        )

        password = input(
            "Password: "
        )

        ip = input(
            "IP Address: "
        )


        login(
            username,
            password,
            ip
        )


    elif choice == "2":

        brute_force_test()


    else:

        print("Invalid option")



if __name__ == "__main__":
    main()
