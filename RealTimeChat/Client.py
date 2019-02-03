import socket
import threading
import time


class Client:

	"""class Client have to handle interaction with server
		send, receive message"""

	# new connection must be initiate
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.message_output = ""
		self.message_input = ""
		self.client_count = 0

	# have to be started 2 new threads for writing and receiving messages
	def init_interaction(self):
		self.sock.connect((self.host, self.port))
		threading.Thread(target=self.writing, args=()).start()
		threading.Thread(target=self.reading, args=()).start()

	# use to check by GUI for new messages
	def get_message(self):
		if self.message_input != "":
			message = self.message_input
			self.message_input = ""
			return message

	# use to send messages by GUI
	def send_message(self, message):
		self.message_output = message
		print(self.message_output)

	# perform sending
	def writing(self):
		while self.sock:
			time.sleep(0.1)
			try:
				if self.message_output == "^q":
					self.message_output = ""
					self.sock.close()
					break
				elif self.message_output != "":
					self.sock.send(self.message_output.encode())
					self.message_output = ""
			except socket.error:
				self.sock.close()
				break

	# perform receiving
	def reading(self):
		while self.sock:
			time.sleep(0.1)
			try:
				data = self.sock.recv(1024)
				if data:
					self.message_input = data
					data = None
			except socket.error:
				self.sock.close()
				break

	# close connection
	def close(self):
		self.sock.close()



