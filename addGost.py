''' 
ex. ./gost -L=tcp://:443 -L=udp://:443 -F=forward+mtls://1.2.3.4:443?mbind=true

Listening type: TCP or UDP
Listening port: ?
Transport protocol: relay or forward
Transport method: ws, wss, mws, mwss, tls, mtls
Target ip address: ?
Target ip port: ?
ws path: /?
mbind type: ?
'''
# range [min, max]
def checkNumRange(userin, min, max):
    # option must be int
    if userin.isdigit():
        if int(userin) >= min and int(userin) <= max:
            return int(userin)
    
    return -1

Ltype = -1
while Ltype == -1:
    print('Choose Listening type:\n1. TCP\n2. UDP\n3. TCP and UDP')

    Ltype = checkNumRange(input("Please have a choice:"), 1, 3)

Lport = -1
while Lport == -1:
    print('Choose Listening port[0-65535]:')
    Lport = checkNumRange(input(), 0, 65535)

TranP = -1
while TranP == -1:
    print('Choose Transport protocol:\n1. relay\n2. forward')
    TranP = checkNumRange(input("Please have a choice:"), 1, 2)
options = ['relay', 'forward']
TranP = options[TranP]

TranM = -1
wsPath = ""
while TranM == -1:
    print('Choose Transport method:\n1. ws\n2.wss\n3.mws\n4.mwss\n5.tls\n6.mtls')
    TranM = checkNumRange(input("Please have a choice:"), 1, 6)
    
if TranM <= 4:
    print("Please input ws path[default '/']\nDon't add '/' just name:")
    wsPath = "&path=/" + input()

options = ['ws', 'wss', 'mws', 'mwss', 'tls', 'mtls']
TranM = options[TranM]

# wsPath = ""
# if TranM <= 4:
#     print("Please input ws path[default '/']\nDon't add '/' just name:")
#     wsPath = "&path=/" + input()


TarIPAddr = -1
while TarIPAddr == -1:
    print("Please input target ip address or domain: ")
    TarIPAddr = input()

TarIPort = -1
while TarIPort == -1:
    print("Please input target port[0-65535]: ")
    TarIPort = checkNumRange(input(), 0, 65535)

ISmbind = -1
while ISmbind == -1:
    print("Please choose mbind True or False:\n1.True\n2.False")
    ISmbind = checkNumRange(input("Please have a choice:"), 1, 2)
options = ['True', 'False']
ISmbind = options[ISmbind-1]


if Ltype == 1:
    print("./gost -L=tcp://:%d -F=%s+%s://%s:%d?mbind=%s%s"%(Lport, TranP, TranM, TarIPAddr, TarIPort, ISmbind, wsPath))    
