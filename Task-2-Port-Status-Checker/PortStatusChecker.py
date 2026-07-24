import socket
import time


def check_port(ip, port, timeout=1):
    """
    Checks the status of a TCP port.
    Returns: Open, Closed, or Filtered
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((ip, port))

        if result == 0:
            status = "Open"
        elif result == 111 or result == 10061:
            status = "Closed"
        else:
            status = "Filtered"

    except socket.timeout:
        status = "Filtered"

    except Exception:
        status = "Filtered"

    finally:
        sock.close()

    return status


def port_scanner():
    print("=" * 60)
    print("            PORT STATUS CHECKER")
    print("=" * 60)

    target = input("Enter Target IP Address: ")

    try:
        start_port = int(input("Enter Starting Port: "))
        end_port = int(input("Enter Ending Port: "))
    except ValueError:
        print("Invalid port number.")
        return

    print("\nScanning...")
    print("-" * 60)

    start_time = time.time()

    print("{:<10} {:<15}".format("PORT", "STATUS"))
    print("-" * 60)

    for port in range(start_port, end_port + 1):
        status = check_port(target, port)
        print("{:<10} {:<15}".format(port, status))

    end_time = time.time()

    print("-" * 60)
    print(f"Scan completed in {round(end_time-start_time,2)} seconds.")


if __name__ == "__main__":
    port_scanner()
