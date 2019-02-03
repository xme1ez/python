Real Time chat contains 3 class files:
- Server.py;
- Client.py;
- ClientWindow.py.
Modules were used: Socket, tkinter, threading, time.
Server class works like echo agent between connected clients, all messages from one client has to be transmitted to others.
Client class perform intercation with Server: sending, receiving messages.
ClientWindow class is GUI for Client class.
Chat can work via the Internet. For the correct operation of the Server, it is necessary to configure the forwarding port. To connect to the Server in the Client, need to specify the server's IP on the Internet and the forwarding port.
