from threading import Thread

from .Functions import Functions
from .Clients import Clients

class ClientListener(Thread):
	def __init__(self, server, addr):
		super(ClientListener, self).__init__()
		self.rootserver = server
		self.addr = addr
		self.user = Clients()()[self.addr]

	def run(self):
		work = True
		while work and self.rootserver._work:
			try:
				data = Functions().get_data(self.user["sock"])
			except:
				work = False
				Clients()().pop(self.addr)
				pattern = "{} disconected({}:{})".format(self.user["data"][0]["name"], self.addr[0], self.addr[1])
				Functions().send_if_condition(self.user["data"][0]["type"] != "echo-test", pattern)
			else:
				pattern = data[1].format(Clients()()[self.addr]["data"][0]["name"], data[0]["massage"])
				if not self.addr in list(Clients().ban_clients):
					Functions().send_if_condition(self.addr, pattern)