import socket

# Creating a Server
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Notice that we passed two parameters here. The first one AF_INET states
# that we want an internet socket rather than a UNIX socket . The second one
# SOCK_STREAM is for the protocol that we choose. In this case it stands for
# TCP . If we wanted UDP , we would have to choose SOCK_DGRAM.

# For the address we will use the localhost address 127.0.0.1 and as a
# port, we will choose 9999.
s.bind(('127.0.0.1',9999))
s.listen()
print('Listening...')

while True:
    client,address = s.accept()
    print('Connected to {}'.format(address))
    message = 'Hello Client!'
    client.send(message.encode('ascii'))
    client.close()