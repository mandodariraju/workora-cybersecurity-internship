import socket
import struct
import datetime


# Log file
LOG_FILE = "network_log.txt"


# Create log function
def write_log(data):

    with open(LOG_FILE, "a") as file:

        file.write(data + "\n")



# Parse IP header
def parse_ip_header(packet):

    ip_header = packet[0:20]

    iph = struct.unpack(
        "!BBHHHBBH4s4s",
        ip_header
    )


    version_ihl = iph[0]

    version = version_ihl >> 4

    protocol = iph[6]


    source_ip = socket.inet_ntoa(
        iph[8]
    )

    destination_ip = socket.inet_ntoa(
        iph[9]
    )


    return (
        source_ip,
        destination_ip,
        protocol
    )



# Parse TCP header
def parse_tcp(packet):

    tcp_header = packet[20:40]


    tcph = struct.unpack(
        "!HHLLBBHHH",
        tcp_header
    )


    source_port = tcph[0]

    destination_port = tcph[1]


    return (
        source_port,
        destination_port
    )



# Parse UDP header
def parse_udp(packet):

    udp_header = packet[20:28]


    udph = struct.unpack(
        "!HHHH",
        udp_header
    )


    source_port = udph[0]

    destination_port = udph[1]


    return (
        source_port,
        destination_port
    )



# Main sniffer

def start_sniffer():

    print("="*60)
    print("          NETWORK PACKET SNIFFER")
    print("="*60)


    # Raw socket

    s = socket.socket(
        socket.AF_INET,
        socket.SOCK_RAW,
        socket.IPPROTO_IP
    )


    host = socket.gethostbyname(
        socket.gethostname()
    )


    s.bind(
        (host, 0)
    )


    s.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_HDRINCL,
        1
    )


    print("\nSniffing started...")
    print("Press CTRL + C to stop\n")


    packet_count = 0


    while True:


        packet, addr = s.recvfrom(65565)


        source, destination, protocol = parse_ip_header(packet)


        packet_count += 1


        timestamp = datetime.datetime.now()


        if protocol == 6:

            src_port, dst_port = parse_tcp(packet)

            protocol_name = "TCP"


            info = (
                f"{timestamp} | "
                f"{protocol_name} | "
                f"{source}:{src_port} --> "
                f"{destination}:{dst_port}"
            )


        elif protocol == 17:

            src_port, dst_port = parse_udp(packet)

            protocol_name = "UDP"


            info = (
                f"{timestamp} | "
                f"{protocol_name} | "
                f"{source}:{src_port} --> "
                f"{destination}:{dst_port}"
            )


        else:

            info = (
                f"{timestamp} | "
                f"Protocol:{protocol} | "
                f"{source} --> {destination}"
            )


        print(info)


        write_log(info)



if __name__ == "__main__":

    start_sniffer()
