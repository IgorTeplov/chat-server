from .Clients import Clients
from .Consol import Consol
from .Functions import Functions

class CommandObj:
	work = True
	def __init__(self, root):
		super(CommandObj, self).__init__()
		self.__root = root

	def start_command_console(self):
		while self.work:
			command = input("Command: ")
			self.command_processor(command)

	def command_processor(self, command):
		opt = command.lstrip().split(" ")
		if not command == "" and opt[0] in self.__class__.__dict__.keys():
			self.__class__.__dict__[opt[0]](self, *opt)

	def help(self, *args):
		Consol().show("system" , "exit")
		Consol().show("system" , "clients")
		Consol().show("system" , "send (host) (port) (massage ...)")
		Consol().show("system" , "sendAll (massage ...)")
		Consol().show("system" , "findOn host (host ...)")
		Consol().show("system" , "ban (host) (port)")
		Consol().show("system" , "unban (host) (port)")
		Consol().show("system" , "baned")

	def exit(self, *args):
		self.work = False

	def clients(self, *args):
		# clients
		# clients name type ...
		if len(args) >= 1:
			for addr, data in Clients()().items():
				if len(args) == 1:
					Consol().show("system" , addr, data["data"][0]["name"])
				elif len(args) > 1:
					Consol().show("system", addr, [data["data"][0][name] for name in args[1:] if name in data["data"][0].keys()])
				
	def send(self, *args):
		# send 127.0.0.1 51478 hi bro ...
		if len(args) > 2:
			if (str(args[1]), int(args[2])) in Clients()().keys():
				for addr, _ in Clients()().items():
					if str(addr[0]) == str(args[1]) and int(addr[1]) == int(args[2]):
						Functions().send(addr, "Server: " + " ".join(args[3:]))
						Consol().show("system", addr, "Server: " + " ".join(args[3:]))

	def sendAll(self, *args):
		if len(args) > 1:
			for addr, _ in Clients()().items():
				Functions().send(addr, "Server: " + " ".join(args[1:]))
			Consol().show("system", addr, "Server: " + " ".join(args[1:]))

	def findOn(self, *args):
		print(args)
		# findOn host 127.0.0.1 ...
		if len(args) >= 2:
			for addr, data in Clients()().items():
				for host in args[2:]:
					if str(addr[0]) == str(host):
						Consol().show("system", addr, data["data"][0]["name"])
		else:
			pass

	def ban(self, *args):
		# ban 127.0.0.1 51478
		if len(args) >= 2:
			for addr, data in Clients()().items():
				if str(addr[0]) == str(args[1]) and int(addr[1]) == int(args[2]):
					Functions().send(addr, "Server: you are baned!")
					Clients().ban_clients[addr] = data
					
	def unban(self, *args):
		# unban 127.0.0.1 51478
		if len(args) >= 2:
			for addr in list(Clients().ban_clients):
				if str(addr[0]) == str(args[1]) and int(addr[1]) == int(args[2]):
					Clients().ban_clients.pop(addr)
					Functions().send(addr, "Server: you are unbaned!")

	def baned(self, *args):
		for addr, data in Clients().ban_clients.items():
			Consol().show("system", addr, data["data"][0]["name"])