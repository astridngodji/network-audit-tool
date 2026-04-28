import socket
import argparse
import time
import threading
from concurrent.futures import ThreadPoolExecutor


total_ports = 0
scanned_ports = 0
lock = threading.Lock()

services = {
                21: "FTP",
                22: "SSH",
                80: "HTTP",
                443: "HTTPS",
                3306: "MySQL"
            }

def scan_port(target, port):
    """Scans a specific port on the target machine."""
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#(uses IPv4, uses TGP connection)
            s.settimeout(1)  # Set timeout for faster scanning

            # Try connecting to the port
            if s.connect_ex((target, port)) ==0:
                service = services.get(port, "Unknown")
                print(f"[+] Port {port} is OPEN - {service}")

    except socket.error:
        pass

    with lock:
        scanned_ports += 1
        
def scan_ports(target, start_port, end_port):
    """Scans a range of ports on the target machine."""
    global scanned_ports, total_ports

    total_ports = end_port - start_port + 1

    print(f"\n[Scanning {target} from port {start_port} to {end_port}]\n")

    rate = 50 # scans per sec
    delay = 1 / rate
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)
            time.sleep(delay) # rate limiting

        while scanned_ports < total_ports:
            print(f"Progress: {scanned_ports}/{total_ports}", end="\r", flush=True)
            time.sleep(0.1)

    ##print(f"Progress: {scanned_ports}/{total_ports}", end="\r", flush=True)
    ##print("Scan complete.")
    
def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")
    args = parser.parse_args()
    

    scan_ports(args.target, args.start_port, args.end_port)

if __name__ == "__main__":
    main()
