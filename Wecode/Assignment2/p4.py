def IP_Format(ip):
    bit_group = ip.split(".")
    for bit in bit_group:
        if int(bit) > 255 or (len(bit) > 1 and bit[0] == "0"):
            return False
    return True

def IP_Filter(str):
    for i in range(1, len(str) - 2): 
        for j in range(i + 1, len(str) - 1): 
            for k in range(j + 1, len(str)): 
                ip = str
                ip = ip[:k] + "." + ip[k:] 
                ip = ip[:j] + "." + ip[j:] 
                ip = ip[:i] + "." + ip[i:] 
                if IP_Format(ip): print(ip)

str = input()
IP_Filter(str)