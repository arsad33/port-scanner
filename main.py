import socket

def port_scan(target_host, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))

        if result == 0:
            print("Port {}: Open".format(port))
        else:
            print("Port {}: Closed".format(port))

#ip given is hackthissite.org
target_host = "137.74.187.100"
ports = [21, 22, 80, 443]

port_scan(target_host, ports)