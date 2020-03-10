import socket

from .Consol import Consol
class Server:
	def get_server(self, host_port_obj):
		self.host_port = host_port_obj
		server_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
		server_obj.bind(host_port_obj)
		server_obj.listen(100)
		Consol().show("server", "Server on {}:{} is up!".format(*host_port_obj))
		return server_obj