import argparse
import socket
from watcher import watch

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--server", action="store_true", dest="serveron", default=False, help="Run as a server")
parser.add_argument("-ip", "--server-ip", dest="ip", default="127.0.0.1", help="Dirección ip del servidor")
parser.add_argument("-p", "--port", dest="port", default="9123", help="Puerto abierto del servidor")

args = parser.parse_args()
port_int = int(args.port)

def server():
	print("[+] Iniciando servidor...")
	servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	servidor.bind((args.ip, port_int))

	servidor.listen(0)

	print(f"[+] Escuchando en {args.ip}:{port_int}")

	c_socket, c_addr = servidor.accept()
	print(f"[+] Nueva conexión de {c_addr[0]}:{c_addr[1]}")

	while True:
		req = c_socket.recv(262144)
		req = req.decode("utf-8")

		if req.lower() == "close":
			c_socket.close()

		splitted_req = req.split(":")
		splitted_path = splitted_req[1].split("\\")
		fp = os.sep.join(splitted_path)

		match splitted_req[0]:
			case "R":
				if os.path.exists(fp):
					os.remove(fp)
					print(f"[+] Archivo eliminado: {fp}")
				else:
					print(f"[+] {fp} no existe!")
			case "N":
				os.makedirs(os.sep.join(splitted_path[:len(splitted_path)-1]), exist_ok=True)
				with open(fp, 'w') as f:
					f.write(splitted_req[2])
				print(f"[+] Archivo creado: {fp}")
			case "M":
				os.makedirs(os.sep.join(splitted_path[:len(splitted_path)-1]), exist_ok=True)
				with open(fp, 'w') as fm:
					fm.write(splitted_req[2])
				print(f"[+] Archivo modificado: {fp}")
			case _:
				print(f"[W] El cliente envió un mensaje desconocido:\n\t{req}")

	c_socket.close()
	servidor.close()
	print("[+] La conexión fue cerrada por el cliente.")

def client(): 
	print("[+] Iniciando cliente...")
	try:
		cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		cliente.connect((args.ip, port_int))

		print(f"[+] Cliente conectado a {args.ip}:{port_int}")

		while True:
			changes = watch()

			# FILE_ACTION:FILE_NAME:FILE_CONTENT
			if changes[1] == "REM":
				cliente.send("R:{}".format(changes[0]).encode("utf-8"))
			else:
				with open(changes[0]) as f:
					cliente.sendall("{}:{}:{}".format(changes[1][0], changes[0], str(f.read())).encode("utf-8"))

	except KeyboardInterrupt:
		cliente.send("close".encode("utf-8"))
		cliente.close()
		print("Conexión cerrada!")

if args.serveron:
	server()
else:
	client()