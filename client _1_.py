from socket import *
import sys


s = socket(AF_INET,SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host,port))
filename = sys.argv[3]



message = "GET /"+filename+" HTTP/1.1\r\n\r\n"

s.send(message.encode())
while True:
	data = s.recv(1024)
	if not data:
		break
	print(data.decode())	


s.close()




