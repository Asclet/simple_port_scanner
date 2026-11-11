import socket

def scan_port_with_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, port))
        
        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode().strip()
        except:
            banner = "cannot grab banner"
        
        sock.close()
        print(f"port {port} open | service {banner[:50]}")
        return True
    except:
        return False

host = input("enter ip: ")
for port in [80, 443, 22, 21]:
    scan_port_with_banner(host, port)
    
