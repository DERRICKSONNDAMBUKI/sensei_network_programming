import socket

target= '0.0.0.0'
def portscan(port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn = s.connect(target,port)
        return True
    except:
        return False

for x in range(1000,8080):
    if(portscan(x)):
        print('Port {} is open!'.format(x))
    else:
        print('Port {} is closed!'.format(x))

# If it succeeds, the function returns True . If we get an error or an
# exception, it returns False .