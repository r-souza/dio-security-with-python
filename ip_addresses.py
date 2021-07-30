import ipaddress
import time

ip = ipaddress.ip_address('192.168.1.1')
network = ipaddress.ip_network('192.168.10.0/24')

def check_ip(ip, network):
    if ipaddress.ip_address(ip) in network:
        return True
    else:
        return False

def show_all_ips():
    for ip in network.hosts():
        print(ip)
        time.sleep(0.01)

def main():
    print(ip)
    print('#' * 80)

    print(network)
    print('#' * 80)

    print(check_ip(ip, network))
    print('#' * 80)
    
    show_all_ips()
    print('#' * 80)

if __name__ == '__main__':
    main()
