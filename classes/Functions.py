import pickle, socket
from .Clients import Clients
from .Consol import Consol

class Functions:
	@staticmethod
	def get_data(from_):
		data = from_.recv(2048)
		return pickle.loads(data)

	@staticmethod
	def send_if_condition(condition, pattern):
		if isinstance(condition, bool):
			for addr, datas in Clients()().items():
				if condition:
					if not addr in list(Clients().ban_clients):
						datas["sock"].sendto(pickle.dumps(pattern), addr)
		else:
			for addr, datas in Clients()().items():
				if condition != addr:
					if not addr in list(Clients().ban_clients):
						datas["sock"].sendto(pickle.dumps(pattern), addr)
		Consol().show("massage", pattern)

	@staticmethod
	def send(addr, pattern):
		Clients()()[addr]["sock"].sendto(pickle.dumps(pattern), addr)