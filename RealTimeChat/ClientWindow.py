import tkinter
import threading
import time
from tkinter import messagebox

import Client as ClientCnct


class ClientWindow:

	"""class ClientWindow (GUI) could be used for
		interaction with Client class."""
	def __init__(self):
		self.chatWindow = tkinter.Tk()
		self.zeroStageFrame = tkinter.Frame()
		self.firstStageFrame = tkinter.Frame()
		self.secondStageFrame = tkinter.Frame()
		self.thirdStageFrame = tkinter.Frame()
		self.fourthStageFrame = tkinter.Frame()
		self.ipLabel = tkinter.Label()
		self.ipField = tkinter.Entry()
		self.portLabel = tkinter.Label()
		self.portField = tkinter.Entry()
		self.connectBtn = tkinter.Button()
		self.yScroll = tkinter.Scrollbar()
		self.messageField = tkinter.Text()
		self.entryField = tkinter.Entry()
		self.sendBtn = tkinter.Button()
		self.statusLabel = tkinter.Label()
		self.client = ClientCnct
		self.connection_status = "disconnected"
		self.count_of_connected_clients = 0

	def init_main_window(self):
		self.chatWindow.geometry('315x520')
		self.chatWindow.title("Real-time Socket chat")
		self.chatWindow.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.zeroStageFrame = tkinter.Frame(self.chatWindow)
		self.zeroStageFrame.grid(row=0, column=1, sticky='news')
		self.firstStageFrame = tkinter.Frame(self.chatWindow)
		self.firstStageFrame.grid(row=1, column=1, sticky='news')
		self.secondStageFrame = tkinter.Frame(self.chatWindow)
		self.secondStageFrame.grid(row=3, column=1, sticky='news')
		self.thirdStageFrame = tkinter.Frame(self.chatWindow)
		self.thirdStageFrame.grid(row=5, column=1, sticky='news')
		self.fourthStageFrame = tkinter.Frame(self.chatWindow)
		self.fourthStageFrame.grid(row=7, column=1, sticky='news')

		self.client_name_label = tkinter.Label(self.zeroStageFrame,
											   text="Your nickname:")
		self.client_name_label.grid(row=0, column=0, sticky='news')
		self.client_name_entry = tkinter.Entry(self.zeroStageFrame, width=15)
		self.client_name_entry.grid(row=0, column=1, sticky='news')
		self.client_name_entry.insert(0, 'xme1ez')

		self.ipLabel = tkinter.Label(self.firstStageFrame, text="IP: ")
		self.ipLabel.grid(row=0, column=0, sticky='news')
		self.ipField = tkinter.Entry(self.firstStageFrame, width=15)
		self.ipField.grid(row=0, column=1, sticky='news')
		self.ipField.insert(0, '93.76.229.14')
		self.portLabel = tkinter.Label(self.firstStageFrame, text="Port: ")
		self.portLabel.grid(row=0, column=2, sticky='news')
		self.portField = tkinter.Entry(self.firstStageFrame, width=5)
		self.portField.grid(row=0, column=4, sticky='news')
		self.portField.insert(0, '10001')
		self.connectBtn = tkinter.Button(self.firstStageFrame, text="connect",
										 command=self.setup_connection)
		self.connectBtn.grid(row=0, column=5, sticky='news')

		self.yScroll = tkinter.Scrollbar(self.secondStageFrame, orient=tkinter.VERTICAL)
		self.yScroll.grid(row=0, column=7, sticky=tkinter.N+tkinter.S)
		self.messageField = tkinter.Text(self.secondStageFrame, state='disabled',
									yscrollcommand=self.yScroll.set, width=36)
		self.messageField.grid(row=0, column=0, sticky='news')
		self.yScroll['command'] = self.messageField.yview()

		self.entryField = tkinter.Entry(self.thirdStageFrame, width=30)
		self.entryField.grid(row=0, column=0, sticky='news')
		self.sendBtn = tkinter.Button(self.thirdStageFrame, text='Send',
									  command=self.send_message)
		self.sendBtn.grid(row=0, column=6, sticky='news')

		self.statusLabel = tkinter.Label(self.fourthStageFrame,
									text=self.process_status_str())
		self.statusLabel.grid(row=0, column=0, sticky='news')
		self.client = ClientCnct.Client(self.get_ip(), int(self.get_port()))
		self.chatWindow.mainloop()

	def process_status_str(self):
		return "status = {} | connected clients: {}".format(self.connection_status,
															str(self.count_of_connected_clients))

	def setup_connection(self):
		self.client = ClientCnct.Client(self.get_ip(), int(self.get_port()))
		self.client.init_interaction()
		threading.Thread(target=self.message_checker, args=()).start()

	def close_connection(self):
		self.client.close()

	def message_checker(self):
		while self.client is not None:
			time.sleep(0.1)
			try:
				mail = self.client.get_message()
				if mail:
					mail = mail.decode('utf8')
					if mail.find('^size&^') != -1 and len(mail) == 8:
						self.count_of_connected_clients = int(mail[7])
					else:
						self.count_of_connected_clients = int(mail[7])
						self.add_message_to_field(mail[9:])
					self.statusLabel['text'] = self.process_status_str()
			except AttributeError:
				pass

	def get_ip(self):
		return self.ipField.get()

	def get_port(self):
		return self.portField.get()

	def get_nickname(self):
		return self.client_name_entry.get()

	def send_message(self):
		self.client.send_message(self.get_nickname()+":"+self.entryField.get())
		self.add_message_to_field("You: " + self.entryField.get())

	def add_message_to_field(self, message=""):
		if message != "":
			print(message)
			self.messageField.config(state="normal")
			self.messageField.insert(tkinter.INSERT, str(message)+"\n")
			self.messageField.config(state="disabled")

	def on_closing(self):
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			self.chatWindow.destroy()
			self.client = None


ClientWindow().init_main_window()
