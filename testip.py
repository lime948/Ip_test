import ipaddress

def ipteszt(ip):
    try:
        ipcim = ipaddress.ip_address(ip)
        
        if ipcim.version == 4:
            return "Az ip cím IPv4 típusú."
        elif ipcim.version == 6:
            return "Az ip cím IPv6 típusú."
    except ValueError:
        return "Helytelen IP cím"

ipcim_input = input("Adjon meg egy ip címet: ")

print(ipteszt(ipcim_input))
#Készítette: Oreskó Zétény (nem volt párom)