from threading import Thread

from .Functions import Functions
from .Clients import Clients
from .Consol import Consol
from .ClientListener import ClientListener

class ServerAccepts(Thread):
	_work = True
	_thread_list = []
	def __init__(self, server_obj):
		super(ServerAccepts, self).__init__()
		self.server = server_obj

	def stop_accepts(self):
		self._work = False

	def run(self):
		while self._work:
			client_sock, client_addr = self.server.accept()
			data = Functions().get_data(client_sock)
			Consol().show("server", data)
			pattern = 'Connected by: {} ({}:{})'.format(data[0]["name"], client_addr[0], client_addr[1])
			Functions().send_if_condition(data[0]["type"] != "echo-test", pattern)
			Clients()()[client_addr] = {
				"sock": client_sock,
				"data": data
			}
			listen_thread = ClientListener(self, client_addr)
			self._thread_list.append(listen_thread)
			listen_thread.setDaemon(daemonic=True)
			listen_thread.start()