import socket
import argparse
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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#(uses IPv4, uses TGP connection)
        s.settimeout(1)  # Set timeout for faster scanning

        # Try connecting to the port
        result = s.connect_ex((target, port))#( Returns 0 if open, an error code if closed.)

        # Check if the port is open
        if result == 0:
            service = services.get(port, "Unknown")
            print(f"[+] Port {port} is OPEN - {service}")
            
        else:
            print(f"[-] Port {port} is CLOSED")
        s.close()
    except socket.error:
        print("[!] Unable to connect to the target.")

def scan_ports(target, start_port, end_port):
    """Scans a range of ports on the target machine."""
    print(f"\n[Scanning {target} from port {start_port} to {end_port}]\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)



def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")
    args = parser.parse_args()
    

    scan_ports(args.target, args.start_port, args.end_port)

if __name__ == "__main__":
    main()
