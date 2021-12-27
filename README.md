#### Network Progamming

network programming . It is about communicating with other applications and devices
via some network.

sockets . They are the endpoints of the communication channels or
basically, the endpoints that talk to each other. The communication may happen in the same process or even across different continents over the internet.

What’s important is that in Python we have different access levels for the network services. At the lower layers, we can access the simple sockets that allow us to use the connection-oriented and connectionless protocols like TCP or UDP, whereas other Python modules like FTP or HTTP are working on a higher layer – the application layer .

we need to know a couple of things in advance:
· Are we using an internet socket or a UNIX socket?
· Which protocol are we going to use?
· Which IP-address are we using?
· Which port number are we using?

Since we want to communicate over a network instead of the operating system, we will stick with the internet socket .

Transmission Control Protocol) and UDP ( User Datagram Protocol). TCP is connection-oriented and more trustworthy than UDP. The chances of losing data are minimal in comparison to UDP. On the other hand, UDP is much faster than TCP.

The IP-address should be the address of the host our application will run on.

For our port we can basically choose any number we with low numbers, since all numbers up to 1024 are numbers from 1024 to 49151 are reserved . If you numbers, you might have some conflicts with other operating system.

# Client-Server Architecture

Notice that we passed two parameters here. The first one AF_INET states that we want an internet socket rather than a UNIX socket . The second one SOCK_STREAM is for the protocol that we choose. In this case it stands for TCP . If we wanted UDP , we would have to choose SOCK_DGRAM.

# SERVER SOCKET METHODS
There are three methods of the socket class that are of high importance for the servers.

# SERVER SOCKET METHODS
# METHOD    DESCRIPTION
bind()      Binds the address that consists of
            hostname and port to the socket

listen()    Waits for a message or a signal

accept()    Accepts the connection with a client


# CLIENT SOCKET METHODS
For the client, there is only one specific and very important method, namely connect . With this method the client attempts to connect to a server which then has to accept this with the respective method.

# OTHER SOCKET METHODS
Also, there are some other socket methods that are quite important in general.
93OTHER SOCKET METHODS
# METHOD        DESCRIPTION
recv()          Receives a TCP message

send()          Sends a TCP message

recvfrom()      Receives a UDP message

sendto()        Sends a UDP message

close()         Closes a socket

gethostname()   Returns hostname of a socket

## Port Scanner
For the address we will use the localhost address 127.0.0.1 and as a port, we will choose 9999 .

# WARNING:
Port scanning is not allowed on any hosts or networks
which you don’t have explicit permission for. Only scan your own
networks or networks for which you were given permission. I don’t
take any liability for what you do with this knowledge, since I warned
you!
