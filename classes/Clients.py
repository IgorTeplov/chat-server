class Clients:
	client = {
	}
	ban_clients = {}
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Clients, cls).__new__(cls)
		return cls.instance

	def __call__(self):
		return self.client