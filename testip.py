import ipaddress

def check_ip_type(ip):
    try:
        ipcim = ipaddress.ip_address(ip)
        
        if ipcim.version == 4:
            return "IPv4"
        elif ipcim.version == 6:
            return "IPv6"
    except ValueError:
        return "Helytelen IP cím"

ip_input = input("Adjon meg egy ip címet: ")

print(check_ip_type(ip_input))
