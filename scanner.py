import sys
import socket
import argparse
from datetime import datetime
import concurrent.futures

def scan_port(target, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Adjust the timeout as needed

    result = sock.connect_ex((target, port))
    sock.close()

    if result == 0:
        results.append(port)

def scan_ports(target, start_port, end_port):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Couldn't resolve the host.")
        return

    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        port_range = range(start_port, end_port + 1)
        futures = [executor.submit(scan_port, target_ip, port, results) for port in port_range]

    try:
        # Wait for all threads to complete
        concurrent.futures.wait(futures)
    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        sys.exit()

    # Sort the results
    results.sort()

    print("Open ports:")
    for port in results:
        print(f"Port {port} is open.")

def main():
    parser = argparse.ArgumentParser(description="Simple concurrent port scanner")
    parser.add_argument("-H", "--host", help="Target IP address or hostname", required=True)
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-a", "--all", action="store_true", help="Scan all ports")

    args = parser.parse_args()

    target = args.host
    start_port = args.start
    end_port = args.end
    scan_all = args.all

    if scan_all:
        start_port = 1
        end_port = 65535  # The maximum port number

    #Banner
    print("-" * 50)
    print("Scanning Target:", target)
    print(f"Scanning ports from {start_port} to {end_port}")
    print("Time Started:", str(datetime.now()))
    print("-" * 50)

    scan_ports(target, start_port, end_port)

if __name__ == "__main__":
    main()