import socket 

host = input(">")
'''port = 443
'''

def port_list():
    return range(1, 1024)

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test = s.connect_ex((host, port))
    if test == 0:
        print(f"port number {port} is open")


 
for port in port_list():

    scan_port(host, port)


'''import socket

target = '66.235.200.147'
port = 443


def scan_port(target, port):
    print(f'Scan Target > {target}')
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Test connection
        test = s.connect_ex((target, port))
        if test == 0:
            print(f'Port {port} is [open]')


if __name__ == '__main__':
    scan_port(target, port)
    '''
