import socket
import socks

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout after 1 second
    try:
        result = sock.connect_ex((host, port))  # connect_ex returns 0 if port is open
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        sock.close()
    except Exception as e:
        print(f"Error connecting to port {port}: {e}")

def set_proxy(proxy_ip, proxy_port):
    try:
        socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
        socket.socket = socks.socksocket
        print(f"Using SOCKS5 proxy: {proxy_ip}:{proxy_port}")
    except Exception as e:
        print(f"Error setting proxy: {e}")

def scan_port_with_proxy(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is OPEN (via proxy)")
        else:
            print(f"Port {port} is CLOSED (via proxy)")
        sock.close()
    except Exception as e:
        print(f"Error connecting to port {port}: {e}")

def ask_anonymous_scan():
    choice = input("Do you want to scan anonymously (via SOCKS5 proxy)? (y/n): ").strip().lower()
    return choice == 'y'

def main():
    target = input("Enter target IP address: ")
    start_port = int(input("Enter starting port number: "))
    end_port = int(input("Enter ending port number: "))

    anonymous = ask_anonymous_scan()
    if anonymous:
        proxy_ip = input("Enter SOCKS5 proxy IP: ")
        proxy_port = int(input("Enter SOCKS5 proxy port: "))
        set_proxy(proxy_ip, proxy_port)
        print("Scanning with SOCKS5 proxy...")
    else:
        print("Scanning normally...")

    for port in range(start_port, end_port + 1):
        if anonymous:
            scan_port_with_proxy(target, port)
        else:
            scan_port(target, port)

if __name__ == "__main__":
    main()
