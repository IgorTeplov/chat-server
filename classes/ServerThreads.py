from .CommandObj import CommandObj
from .ServerAccepts import ServerAccepts

from threading import Thread
class ServerThreads:
	base = {}

	def __init__(self, host_port):
		self.host_port = host_port

	def create_thread_from_server_obj(self, server_obj, id_):
		server_thread = ServerAccepts(server_obj)
		server_thread.setDaemon(daemonic=True)
		self.base[id_] = server_thread
	
	def start_server_thread_by_id(self, id_):
		self.base[id_].start()
		# Thread(target=union_connect, args=(self.host_port), daemon=True).start()
		CommandObj(self).start_command_console()

	def __dict__(self):
		return self.base