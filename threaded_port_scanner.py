# In order to speed up the scanning process, we are going to use multithreading
# . And to make sure that every port gets scanned and also that no port is
# scanned twice, we will use queues.

import socket
from queue import Queue
import threading

target = '0.0.0.0'
q=Queue()
for x in range (8000,9000):
    q.put(x)

def portscan(port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn = s.connect((target,port))
        return True
    except:
        return False

def worker():
    while True:
        port = q.get()
        if portscan(port):
            print('Port {} is open!'.format(port))

for x in range(30):
    t=threading.Thread(target=worker())
    t.start()