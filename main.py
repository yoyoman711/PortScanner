import socket
import threading
import argparse


# Function to scan single port
def port_scan(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")

    except Exception as e:
        pass

# function for handling port range
def port_scanner(ip, start_port, end_port, threads):
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    thread_list = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=port_scan, args=(ip, port))
        thread_list.append(thread)
        thread.start()
        if len(thread_list) >= threads:
            for t in thread_list:
                t.join()
            thread_list = []

    # Wait for threads to complete
    for t in thread_list:
        t.join()
    print("Scan complete")


# Main Function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("ip", help="IP address to scan")
    parser.add_argument("start_port", type=int, help="Start of port range")
    parser.add_argument("end_port", type=int, help="End of port range")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads (default:10)")

    args = parser.parse_args()

    port_scanner(args.ip, args.start_port, args.end_port, args.threads)
