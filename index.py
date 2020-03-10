from classes.GetHostPort import GetHostPort
from classes.Server import Server
from classes.ServerThreads import ServerThreads

def main(id_):
	server_full_obj = Server()
	server_obj = server_full_obj.get_server(GetHostPort()())
	server = ServerThreads(server_full_obj.host_port)
	server.create_thread_from_server_obj(server_obj, id_)
	server.start_server_thread_by_id(id_)

if __name__ == '__main__':
	main("v1.0.2")
