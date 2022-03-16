import socket
from IPy import IP

def scanner(ipaddress):
    converted_ip = check_ip(ipaddress)
    print('\n' + '[__ + scanning target + __] ' '\n' +str(ipaddress))
    print('\n''[+] Port No ' '\t\t\t' 'version')
    for port in range(1, 65535):
        scan_port(ipaddress, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_version(s):
    return s.recv(1024)

def scan_port(ipaddress , port):
    try:
        sock = socket.socket()
        sock.settimeout(0.7)
        sock.connect((ipaddress , port))
        try:
            version = get_version(sock)
            print('[+] Port '+ str(port) + ' is open' '\t\t'+ str(version.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is open')
    except:
        pass

ipaddress = input('[+] Enter the target to scan (split multiple target with ,):')
if ',' in ipaddress:
    for ip_add in ipaddress.split(','):
        scanner(ip_add.strip(' '))
else:
    scanner(ipaddress)