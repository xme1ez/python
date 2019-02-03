import socket
import threading
import time


class Server(object):

	"""class Server could be used like the echo agent between client.
		client app should be connected to Server by IP and Port.
		Message from one client will be send to other connected clients"""

	# initialization Server parameters. Creation socket object and binding
	# IP and port
	def __init__(self, port, host='0.0.0.0'):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
		self.dict_of_clients = {}
		self.new_client_flag = True

	# "listen" wait for new connection from client, pass connected
	# client to separate thread. if client is inactive during 300
	# seconds - connection have to be interrupt
	def listen(self):

		self.sock.listen(9)

		while True:
			conn_info, addr = self.sock.accept()
			conn_info.settimeout(300)
			# start thread to listen new client
			threading.Thread(target=self.listen_to_client, args=(conn_info, addr)).start()

	# each connection have to be processed. message must be read and parsed.
	# info about each connection must be saved to dictionary:
	# {nickname: connection info}. received message must be resend to other
	# connected clients. few exception must be handled.
	def listen_to_client(self, conn_info, addr):
		size = 1024
		while True:
			time.sleep(0.1)
			try:
				data = conn_info.recv(size)
				msg = str(data[0:len(str(data))])
				msg = msg[msg.find('|')+1:]
				nickname = msg[:msg.find(':')]

				# check if connected client is exist in a list by ip
				for key in self.dict_of_clients.keys():
					if addr[0] in str(self.dict_of_clients[key]) and nickname == key:
						self.new_client_flag = False
				# if current client in't exist at list -> append his info
				if self.new_client_flag:
					self.dict_of_clients[nickname] = conn_info
				self.new_client_flag = True

				if data:
					print(addr[0]+"|"+str(data))
					for client_name, client_addr in self.dict_of_clients.items():

						if nickname != client_name:
							self.dict_of_clients[client_name].send(bytes("^size&^" + str(len(self.dict_of_clients)) + "|" +
												 addr[0] +"|", 'utf-8')+data)

						else:
							self.dict_of_clients[client_name].send(bytes("^size&^" + str(len(self.dict_of_clients)), 'utf-8'))

				else:
					print('Client disconnected')
					self.del_from_client_dict(conn_info)

					break
			except socket.timeout:

				self.del_from_client_dict(conn_info)

				break
			except socket.error:
				self.del_from_client_dict(conn_info)

				break

	def del_from_client_dict(self, conn_info):
		for key, value in self.dict_of_clients.items():
			if conn_info == value:
				del self.dict_of_clients[key]
				break
		conn_info.close()
